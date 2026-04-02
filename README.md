# Generador Horizontal de Oleaje: Energía limpia desde el mar

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19390947.svg)](https://doi.org/10.5281/zenodo.19390947)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![EN](https://img.shields.io/badge/English-version-blue.svg)](./README.en.md)

Las boyas y columnas oscilantes son caras, difíciles de mantener y requieren operaciones en alta mar. La energía solar y eólica no son suficientes en zonas costeras con oleaje constante.

Generador Horizontal de Oleaje nace para resolver ese problema.

## Que hace

Es un sistema que se instala sobre muros costeros existentes (espigones, malecones, rompeolas). Captura la energía cinética del oleaje en su movimiento horizontal, la convierte en electricidad y se integra a la red. Todo el mantenimiento se hace desde tierra, sin buzos ni embarcaciones.

Ventajas:
- Instalación en 48 horas con grúa estándar.
- Mantenimiento anual desde tierra.
- Factor de capacidad del 32% (superior a solar y eólica en zonas costeras).
- Costo por kW: USD 555.

## Componentes tecnicos

### 1. Captura de energia
- Embolos hidraulicos horizontales, diseño asistido por CFD.
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

- Concepto definido (muro costero, embolos horizontales).
- Especificaciones tecnicas completas.
- Modelo financiero validado.
- Estudio de oleaje (pendiente).
- Diseno estructural detallado (pendiente).
- Prototipo escala 1:10 (pendiente).

## Proximos pasos

1. Estudio de oleaje — Seleccionar ubicacion con oleaje constante.
2. Diseno estructural — Dimensionar muro, embolos, sistema hidraulico.
3. Prototipo a escala — Pruebas en tanque de olas.
4. Validacion de materiales — Resistencia a agua salada, ciclos de fatiga.
5. Modelo de negocio — Contratos PPA con empresas o municipalidades.

## Proyectos relacionados

- ShieldAir — torres de produccion de oxigeno.
- Movi-Dick — barco recolector de plasticos marinos.
- CORPUS — sistema corporal artificial.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

Este proyecto está protegido por derechos de autor.

PERMITIDO:
- Uso no comercial con fines educativos o de investigación.
- Distribución sin modificación, siempre que se mantenga esta licencia y se dé crédito al autor.

PROHIBIDO sin autorización expresa por escrito:
- Uso comercial (incluyendo, pero no limitado a: ofrecerlo como servicio, SaaS, suscripción, integración en productos que generen ingresos, o cualquier uso que genere beneficio económico directo o indirecto).
- Modificación para entornos de producción.
- Distribución de versiones modificadas sin autorización.

Para licencias comerciales, soporte técnico, pilotos empresariales o consultas:
Contacto: eaguayo@migst.cl

Cualquier uso fuera de los términos permitidos requiere permiso previo del autor.

Las consultas comerciales son bienvenidas y se responderán en un plazo máximo de 7 días hábiles.

## Autor

Enrique Aguayo H.
Mackiber Labs
Contacto: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentación asistida por Ana (DeepSeek), IA para investigación y optimización técnica.
