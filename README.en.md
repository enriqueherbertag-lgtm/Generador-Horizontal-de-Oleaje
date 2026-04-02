# Horizontal Wave Generator: Clean energy from the sea

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19390947.svg)](https://doi.org/10.5281/zenodo.19390947)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![ES](https://img.shields.io/badge/Spanish-version-green.svg)](./README.md)

Buoys and oscillating columns are expensive, difficult to maintain, and require offshore operations. Solar and wind power are not sufficient in coastal areas with constant waves.

Horizontal Wave Generator was created to solve that problem.

## What it does

It is a system installed on existing coastal walls (breakwaters, jetties, seawalls). It captures the kinetic energy of waves in their horizontal motion, converts it into electricity, and connects to the grid. All maintenance is done from land, without divers or vessels.

Advantages:
- Installation in 48 hours with standard crane.
- Annual maintenance from land.
- Capacity factor of 32% (higher than solar and wind in coastal areas).
- Cost per kW: USD 555.

## Technical components

### 1. Energy capture
- Horizontal hydraulic pistons, CFD-assisted design.
- Materials: Naval steel ASTM A572 with ceramic coatings, or FRP nano-reinforced composites.

### 2. Hydraulic transmission
- Axial piston pumps (>92% efficiency) in closed circuit.
- Hydraulic accumulator to smooth intermittency.
- Proportional valves controlled by PLC.

### 3. Power generation
- Brushless PMSG, low speed (<300 rpm), efficiency >94%.
- Power electronics with wave-adaptive MPPT.
- Output: 480 V DC or 690 V AC.

### 4. Control and monitoring
- Industrial PLC with wave prediction algorithm.
- Sensors: accelerometers, pressure, flow, load cells.
- Communications: 5G, Starlink, or LoRaWAN.

### 5. Grid integration
- Modular coastal substation in ISO 20 container.
- LiFePO4 backup battery (50–300 kWh).
- Compliant with IEEE 1547 / IEC 61727.

## Key specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Installed power | 86.4 kW | Piston cluster |
| Number of pistons | 6–12 | Depending on wave conditions |
| Piston stroke | 0.5–1.5 m | Depending on typical waves |
| Capacity factor | 0.28–0.35 | Estimated |
| Useful life | 20–25 years | With scheduled maintenance |

## Financial model

| Parameter | Value |
|-----------|-------|
| Total investment (86.4 kW cluster) | USD 48,000 |
| Cost per kW | USD 555 |
| Estimated annual energy | 242,275 kWh |
| Annual revenue (PPA @ USD 0.17/kWh) | USD 41,187 |
| Annual OPEX | USD 5,000 |
| Net annual profit | USD 25,700 |
| Simple ROI | 1.3 years |
| IRR (10 years) | > 50% |
| Total estimated profit (25 years) | USD 856,675 |

## Installation and maintenance

### Installation (48 hours)
1. Topographic and structural survey of the existing wall.
2. Mechanical fixing with post-installed anchor bolts.
3. Electrical connection to coastal substation.
4. Startup and grid synchronization.

### Maintenance (from land)
- Annual: inspection, testing, calibration.
- Every 5 years: seal replacement and lubrication.
- Every 10 years: generator overhaul.

No diving or vessels required.

## Current status

- Concept defined (coastal wall, horizontal pistons).
- Complete technical specifications.
- Validated financial model.
- Wave study (pending).
- Detailed structural design (pending).
- 1:10 scale prototype (pending).

## Next steps

1. Wave study — Select location with consistent waves.
2. Structural design — Size wall, pistons, hydraulic system.
3. Scale prototype — Wave tank testing.
4. Material validation — Salt water resistance, fatigue cycles.
5. Business model — PPA contracts with companies or municipalities.

## Related projects

- ShieldAir — oxygen production towers.
- Movi-Dick — plastic collection ship.
- CORPUS — artificial body system.

## License

Copyright © 2026 Enrique Aguayo. All rights reserved.

[Standard proprietary license text...]

## Author

Enrique Aguayo H.
Mackiber Labs
Contact: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentation assisted by Ana (DeepSeek), AI for research and technical optimization.
