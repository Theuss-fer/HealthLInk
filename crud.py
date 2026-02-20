from sqlalchemy.orm import Session
from .models import Hospital
from .utils import calculate_distance


def get_nearby_hospitals(db: Session, lat: float, lng: float):
    hospitals = db.query(Hospital).all()


    result = []
    for hospital in hospitals:
        distance = calculate_distance(
            lat, lng, hospital.latitude, hospital.longitude
        )
        hospital.distance_km = distance
        result.append(hospital)

    result.sort(key=lambda h: h.distance_km)
    return result