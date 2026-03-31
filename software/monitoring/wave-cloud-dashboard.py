#!/usr/bin/env python3
"""
Wave-Cloud Monitoring Dashboard
Sistema de telemetria para Wave-Wall
"""

import json
import time
import sqlite3
from datetime import datetime
from flask import Flask, render_template, jsonify
import requests
import threading

app = Flask(__name__)

# Configuracion
MODBUS_HOST = '192.168.1.100'
MODBUS_PORT = 502
SATELLITE_API = 'https://api.starlink.com/v1/telemetry'
DB_PATH = '/var/lib/wavecloud/data.db'

class WaveWallMonitor:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.init_db()
        self.running = True
        self.data = {
            'power': 0.0,
            'energy_today': 0.0,
            'wave_height': 0.0,
            'wave_period': 0.0,
            'pressure': 0.0,
            'temperature': 0.0,
            'status': 'offline'
        }
    
    def init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS telemetry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                power REAL,
                energy_today REAL,
                wave_height REAL,
                wave_period REAL,
                pressure REAL,
                temperature REAL,
                status TEXT
            )
        ''')
        self.conn.commit()
    
    def read_modbus(self):
        """
        Leer datos del PLC via Modbus TCP
        Implementar con pymodbus o similar
        """
        # Placeholder - implementar con libreria real
        try:
            # from pymodbus.client import ModbusTcpClient
            # client = ModbusTcpClient(MODBUS_HOST, port=MODBUS_PORT)
            # client.connect()
            # power = client.read_holding_registers(0, 1).registers[0] / 10.0
            # client.close()
            # return power
            
            # Simulacion para demostracion
            import random
            return {
                'power': random.uniform(2.0, 10.0),
                'wave_height': random.uniform(0.5, 2.5),
                'wave_period': random.uniform(5.0, 9.0),
                'pressure': random.uniform(160.0, 200.0),
                'temperature': random.uniform(40.0, 70.0)
            }
        except Exception as e:
            print(f"Error reading Modbus: {e}")
            return None
    
    def update(self):
        """Ciclo principal de actualizacion"""
        while self.running:
            try:
                # Leer datos del PLC
                values = self.read_modbus()
                if values:
                    self.data.update(values)
                    self.data['status'] = 'online'
                    self.data['energy_today'] += self.data['power'] * (1.0 / 3600.0)
                else:
                    self.data['status'] = 'offline'
                
                # Guardar en base de datos
                cursor = self.conn.cursor()
                cursor.execute('''
                    INSERT INTO telemetry (timestamp, power, energy_today, wave_height, wave_period, pressure, temperature, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    datetime.now().isoformat(),
                    self.data['power'],
                    self.data['energy_today'],
                    self.data['wave_height'],
                    self.data['wave_period'],
                    self.data['pressure'],
                    self.data['temperature'],
                    self.data['status']
                ))
                self.conn.commit()
                
                # Enviar a satelite si hay conexion
                self.send_to_satellite()
                
            except Exception as e:
                print(f"Update error: {e}")
            
            time.sleep(10)  # Actualizar cada 10 segundos
    
    def send_to_satellite(self):
        """Enviar datos via Starlink API"""
        try:
            payload = {
                'device_id': 'wavewall_001',
                'timestamp': datetime.now().isoformat(),
                'power_kw': self.data['power'],
                'energy_kwh': self.data['energy_today'],
                'wave_height_m': self.data['wave_height'],
                'status': self.data['status']
            }
            # requests.post(SATELLITE_API, json=payload, timeout=5)
            print(f"Satellite data sent: {payload}")
        except Exception as e:
            print(f"Satellite send failed: {e}")

# Iniciar monitor en hilo separado
monitor = WaveWallMonitor()
thread = threading.Thread(target=monitor.update, daemon=True)
thread.start()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/current')
def api_current():
    return jsonify(monitor.data)

@app.route('/api/history')
def api_history():
    cursor = monitor.conn.cursor()
    cursor.execute('SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 100')
    rows = cursor.fetchall()
    return jsonify([{
        'timestamp': r[1],
        'power': r[2],
        'energy_today': r[3],
        'wave_height': r[4],
        'status': r[8]
    } for r in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
