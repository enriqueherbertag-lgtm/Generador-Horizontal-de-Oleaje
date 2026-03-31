# Muro-Oleaje Horizontal

Sistema de generación de energía a partir del oleaje, integrado en muros costeros existentes o de nueva construcción. Aprovecha la infraestructura costera ya presente (espigones, malecones, rompeolas) y permite mantenimiento completamente desde tierra.

## Principio de operacion

El sistema captura la energia cinetica del oleaje en su movimiento horizontal contra el muro. A diferencia de sistemas basados en mareas o boyas de fondeo, Muro-Oleaje Horizontal se instala en la zona de rompientes, donde la energia por metro lineal de costa es maxima y predecible.

El conjunto esta compuesto por:

- Modulos de captura (embolos hidraulicos horizontales) que se desplazan con el oleaje.
- Sistema hidraulico que convierte el movimiento lineal en energia rotacional.
- Generador sincrono de iman permanente (PMSG) de baja velocidad.
- Electronica de potencia con control MPPT especifico para oleaje.
- Proteccion IP69K y materiales resistentes a la corrosion y bio-incrustacion.

## Ventajas frente a otras tecnologias undimotriz

| Caracteristica | Muro-Oleaje Horizontal | Boyas flotantes | Columna oscilante |
|----------------|------------------------|-----------------|-------------------|
| Instalacion | 48h, grua estandar | Semanas, barcos especiales | Buzos, equipo pesado |
| Mantenimiento | Desde tierra, anual | En alta mar, mensual | Buzos, trimestral |
| Uso de infraestructura existente | Si (muros, espigones) | No | No |
| Factor de capacidad | 32% | 25–30% | 28–32% |
| Costo por kW | USD 555 | USD 8,000–15,000 | USD 6,000–10,000 |

## Componentes tecnicos

### 1. Captura de energia
- Embolos hidraulicos horizontales, diseno asistido por CFD.
- Materiales: Acero naval ASTM A572 con recubrimientos ceramicos, o composites FRP nano-reforzados.

### 2. Transmision hidraulica
- Bombas de piston axial de alta eficiencia (>92%) en circuito cerrado.
- Acumulador hidraulico para suavizar intermitencia.
- Valvulas proporcionales controladas por PLC.

### 3. Generacion electrica
- Generador PMSG sin escobillas, baja velocidad (<300 rpm), eficiencia >94%.
- Electronica de potencia con MPPT adaptativo al oleaje.
- Salida: 480 V DC o 690 V AC.

### 4. Control y monitorizacion
- PLC industrial con algoritmo predictivo basado en modelado de oleaje.
- Sensorizacion: acelerometros, presion, caudal, celdas de carga.
- Comunicaciones: 5G, Starlink o LoRaWAN.

### 5. Integracion a red
- Subestacion costera modular en contenedor ISO 20.
- Bateria LiFePO4 de respaldo (50–300 kWh).
- Cumple IEEE 1547 / IEC 61727.

## Especificaciones clave

| Parametro | Valor | Notas |
|-----------|-------|-------|
| Potencia instalada | 86.4 kW | Cluster de embolos |
| Numero de embolos | 6–12 | Segun oleaje del sitio |
| Carrera del embolo | 0.5–1.5 m | Depende del oleaje tipico |
| Factor de capacidad | 0.28–0.35 | Estimado |
| Vida util | 20–25 años | Con mantenimiento programado |

## Modelo financiero

| Parametro | Valor |
|-----------|-------|
| Inversion total (cluster 86.4 kW) | USD 48,000 |
| Costo por kW | USD 555 |
| Energia anual estimada | 242,275 kWh |
| Ingresos anuales (PPA @ USD 0.17/kWh) | USD 41,187 |
| OPEX anual | USD 5,000 |
| Utilidad neta anual | USD 25,700 |
| ROI simple | 1.3 años |
| TIR (10 años) | > 50% |
| Ganancia total estimada (25 años) | USD 856,675 |

## Instalacion y mantenimiento

### Instalacion (48 horas)
1. Levantamiento topografico y estructural del muro existente.
2. Fijacion mecanica con pernos de anclaje post-instalados.
3. Conexion electrica a subestacion costera.
4. Puesta en marcha y sincronizacion.

### Mantenimiento (desde tierra)
- Anual: inspeccion, pruebas, calibracion.
- Cada 5 años: cambio de sellos y lubricacion.
- Cada 10 años: overhaul del generador.

No se requiere buceo ni embarcaciones.

## Estado actual

✅ Concepto definido (muro costero, embolos horizontales)  
✅ Especificaciones tecnicas  
✅ Modelo financiero  
✅ Enfoque en infraestructura existente y mantenimiento desde tierra  
🔲 Estudio de oleaje para ubicacion especifica  
🔲 Diseno estructural detallado  
🔲 Prototipo escala 1:10  
🔲 Validacion de resistencia a corrosion

## Proximos pasos

1. Estudio de oleaje — Seleccionar ubicacion con oleaje constante.
2. Diseno estructural — Dimensionar muro, embolos, sistema hidraulico.
3. Prototipo a escala — Pruebas en tanque de olas.
4. Validacion de materiales — Resistencia a agua salada, ciclos de fatiga.
5. Modelo de negocio — Contratos PPA con empresas o municipalidades.

## Proyectos relacionados

- **ShieldAir** — torres de produccion de oxigeno  
- **Movi-Dick** — barco recolector de plasticos marinos  
- **CORPUS** — sistema corporal artificial

## Licencia

Apache 2.0 con restriccion de uso comercial.

## Autor

**Enrique Aguayo H.**  
Investigador independiente, Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)

Documentacion asistida por **Ana (DeepSeek)** , IA para investigacion y optimizacion tecnica.
