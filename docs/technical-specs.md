# Especificaciones tecnicas Wave-Wall

## Modelos disponibles

| Modelo | Longitud | Potencia continua | Potencia pico | Peso | Aplicacion tipica |
|--------|----------|-------------------|---------------|------|-------------------|
| WW-4000 | 4 m | 5.4 kW | 12 kW | 3200 kg | Muros pequenos, malecones urbanos |
| WW-8000 | 8 m | 10.8 kW | 24 kW | 6200 kg | Espigones, caletas pesqueras |
| WW-12000 | 12 m | 16.2 kW | 36 kW | 9300 kg | Puertos, proteccion costera extensa |

## Componentes mecanicos

### Paletas de captura
- Material: Acero naval ASTM A572 Grado 50 con recubrimiento ceramico
- Alternativa: Composite FRP con refuerzo de fibra de carbono
- Geometria: Perfil hidrodinamico variable asistido por CFD
- Vida util: 25 años

### Sistema hidraulico
- Bombas: Pistones axiales, desplazamiento variable, eficiencia >92%
- Acumulador: Membrana de 20L, presion maxima 250 bar
- Valvulas: Proporcionales, tiempo de respuesta <50 ms
- Fluido: Aceite biodegradable ISO VG 46

### Anclajes
- Tipo: Pernos post-instalados Hilti HDA o equivalente
- Profundidad: 250 mm en hormigon armado
- Carga de diseno: 50 kN por punto
- Certificacion: Sismica (Zona 3, Chile)

## Componentes electricos

### Generador PMSG
- Tipo: Iman permanente sin escobillas
- Velocidad nominal: 250 rpm
- Potencia nominal: 12 kW (WW-8000)
- Eficiencia: 94% a carga nominal
- Proteccion: IP69K

### Electronica de potencia
- Inversor: Bidireccional, 480 V DC / 400 V AC
- MPPT: Algoritmo adaptativo con prediccion de oleaje
- Protecciones: Sobrevoltaje, sobrecorriente, cortocircuito, isla no intencional
- Comunicacion: Modbus TCP/IP

### Subestacion costera (SCM-200)
- Dimensiones: Contenedor ISO 20 pies (6.1 x 2.4 x 2.6 m)
- Capacidad: Hasta 200 kW continuos
- Bateria: LiFePO4, 200 kWh, IP55
- Transformador: 480 V DC / 13.2 kV AC, 3 fases
- EMS: Siemens S7-1500 con modulo AI Edge
- Comunicacion: 5G + Starlink + LoRaWAN

## Condiciones ambientales

| Parametro | Rango operativo |
|-----------|-----------------|
| Temperatura ambiente | -10°C a +45°C |
| Altura de ola significativa | 0.5 m a 3.5 m |
| Periodo de ola | 4 s a 12 s |
| Profundidad minima | 3 m |
| Corrosividad | C5 (ambiente marino extremo) |

## Normativas aplicables

- IEC TS 62600-2: Marine energy - Wave energy converters
- IEC 61400-3: Wind turbines - Offshore (adaptado)
- IEEE 1547: Interconnection of distributed energy resources
- UL 1741: Inverters and converters
- NCh Elec 4/2003: Instalaciones electricas en Chile
