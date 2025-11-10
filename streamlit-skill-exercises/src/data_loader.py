from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_CARS: Dict[str, Dict[str, Any]] = {
    "Ferrari f40 (1987)": {"logo": "assets/ferrari_logo.svg", "performance": {"0_100_kmh": 4.0, "0_200_kmh": 10.4, "0_300_kmh": 31.0}},
    "Ferrari 488 GTB (2015)": {"logo": "assets/ferrari_logo.svg", "performance": {"0_100_kmh": 2.8, "0_200_kmh": 8.1, "0_300_kmh": 23.9}},
    "Ford Mustang GT (2010)": {"logo": "assets/ford_logo.svg", "performance": {"0_100_kmh": 5.8, "0_200_kmh": 21.3}},
    "Ford Mustang SVT Cobra (1996)": {"logo": "assets/ford_logo.svg", "performance": {"0_100_kmh": 5.4, "0_200_kmh": 22.5}},
    "BMW M3 Competition (F80) (2016)": {"logo": "assets/bmw_logo.svg", "performance": {"0_100_kmh": 4.0, "0_200_kmh": 13.2}},
    "BMW M5 Competition (F10) (2013)": {"logo": "assets/bmw_logo.svg", "performance": {"0_100_kmh": 4.1, "0_200_kmh": 12.3}},
    "Mercedes - AMG GT 63 S E Performance (C192) (2024)": {"logo": "assets/amg_logo.svg", "performance": {"0_100_kmh": 2.8, "0_200_kmh": 9.3}},
    "Mercedes - AMG C63 S E Performance T-Modell (2022)": {"logo": "assets/amg_logo.svg", "performance": {"0_100_kmh": 3.3, "0_200_kmh": 12.4}},
}


def _normalize(entry: Any) -> Dict[str, Any]:
    if not isinstance(entry, dict):
        return {"logo": None, "performance": {}}
    perf = {}
    raw_perf = entry.get("performance", {})
    if isinstance(raw_perf, dict):
        for k, v in raw_perf.items():
            try:
                perf[str(k)] = float(v)
            except (TypeError, ValueError):
                continue
    return {"logo": entry.get("logo"), "performance": perf}


def load_cars_data(path: Optional[Union[str, Path]] = None) -> Dict[str, Dict[str, Any]]:
    """
    Carga el JSON de coches y devuelve un dict normalizado.
    - path: ruta al JSON. Si None usa ../data/cars.json relativo a este archivo.
    - Si falta o está corrupto devuelve DEFAULT_CARS.
    """
    if path is None:
        path = Path(__file__).resolve().parents[1] / "data" / "cars.json"
    else:
        path = Path(path)

    if not path.exists():
        return DEFAULT_CARS

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return DEFAULT_CARS

    if not isinstance(raw, dict):
        return DEFAULT_CARS

    return {name: _normalize(entry) for name, entry in raw.items()}
