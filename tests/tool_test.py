from mlproject.distance import haversine
import mlproject

def test_assert():
    assert haversine(40.7486, -73.9864, 51.8853, 0.2545) == 8289.57366475712
