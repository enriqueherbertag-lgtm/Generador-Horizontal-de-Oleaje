# Procedimiento de mantenimiento Wave-Wall

## Frecuencias

| Intervalo | Actividades |
|-----------|-------------|
| Mensual | Inspeccion visual remota (camaras), verificacion de datos de telemetria |
| Trimestral | Inspeccion in situ, limpieza de sensores, prueba de actuadores |
| Anual | Cambio de filtros hidraulicos, analisis de aceite, calibracion de valvulas |
| 5 años | Cambio de sellos hidraulicos, lubricacion de rodamientos, prueba de hermeticidad |
| 10 años | Overhaul del generador, recertificacion de anclajes, inspeccion con ultrasonido |

## Mantenimiento anual (detallado)

### Equipos necesarios
- Grua movil 15 ton
- Analizador de aceite
- Multimetro de precision
- Camara termografica
- Kit de sellos de repuesto

### Procedimiento

1. **Aislamiento electrico**
   - Desconectar inversor de la red
   - Bloquear seccionador con candado
   - Verificar ausencia de tension

2. **Izaje del modulo de generacion**
   - Instalar eslingas en puntos designados
   - Elevar 30 cm y verificar nivelacion
   - Retirar modulo y depositar en area de trabajo

3. **Inspeccion mecanica**
   - Verificar desgaste de paletas (espesor minimo 12 mm)
   - Medir holgura en rodamientos (maximo 0.5 mm)
   - Inspeccion visual de sellos hidraulicos

4. **Analisis de aceite hidraulico**
   - Tomar muestra de 200 mL
   - Medir viscosidad (rango: 40-50 cSt a 40°C)
   - Analisis espectrografico de desgaste (Fe, Cu, Si)
   - Cambiar si acidez >1.5 mg KOH/g

5. **Pruebas electricas**
   - Resistencia de aislamiento (>1 MOhm a 500 V DC)
   - Resistencia de bobinados (desviacion <5% respecto a placa)
   - Corriente de fuga (<10 mA)

6. **Calibracion de sensores**
   - Acelerometros: excitacion con shaker de referencia
   - Celdas de carga: aplicacion de peso conocido
   - Sensores de presion: comparacion con manometro patron

7. **Limpieza y proteccion**
   - Eliminar bio-incrustacion con cepillo de cerdas duras
   - Aplicar recubrimiento anticorrosivo en puntos detectados
   - Verificar estanqueidad de prensaestopas

8. **Reinstalacion y pruebas**
   - Montar modulo en sentido inverso
   - Torquear pernos a 450 Nm
   - Realizar prueba de hermeticidad (presion positiva 0.5 bar)
   - Ejecutar secuencia de partida en vacio

## Registro de mantenimiento

Cada intervencion debe quedar registrada en formato digital con:

- Fecha y hora
- Personal responsable
- Mediciones realizadas
- Componentes reemplazados
- Observaciones y desviaciones

Los registros se almacenan en la plataforma Wave-Cloud con acceso a personal autorizado.

## Indicadores de mantenimiento

| Indicador | Meta |
|-----------|------|
| Disponibilidad | >95% |
| Tiempo medio entre fallas (MTBF) | >5000 horas |
| Tiempo medio de reparacion (MTTR) | <8 horas |
| Costo anual de mantenimiento | <5% del CAPEX |
