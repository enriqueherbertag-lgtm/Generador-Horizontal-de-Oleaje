# Simulaciones Wave-Wall

Este directorio contiene los archivos de simulacion utilizados para validar el diseno del sistema.

## CFD (Computational Fluid Dynamics)

- **software**: ANSYS Fluent / OpenFOAM
- **dominio**: 100m x 50m x 20m (largo x ancho x profundidad)
- **malla**: 2.5 millones de elementos, refinamiento en zona de rompientes
- **condiciones**: Olas regulares e irregulares (JONSWAP)
- **archivos**: wave-loads.cas (caso base), wave-loads.dat (resultados)

## MEF (Finite Element Method)

- **software**: ANSYS Mechanical / Abaqus
- **modelo**: Estructura completa Wave-Wall, anclajes, muro existente
- **cargas**: Presiones hidrodinamicas desde CFD, peso propio, sismo (NCh433)
- **resultados**: Deformaciones, tensiones, factor de seguridad
- **archivos**: fem-analysis.fem, fem-analysis.rpt

## Validacion

Las simulaciones fueron validadas con:
- Datos de boyas DART (Deep-ocean Assessment and Reporting of Tsunamis)
- Mediciones de campo en rompeolas de Valparaiso (SHOA)
- Ensayos en canal de olas a escala 1:20 (UTFSM)

Los archivos de simulacion se encuentran disponibles bajo solicitud debido a su tamano.
