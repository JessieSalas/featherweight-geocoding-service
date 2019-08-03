#!/bin/sh
echo "Demo Apple Campus: 1 Infinite Loop, Cupertino"
curl -d '{"query":"1 Infinite Loop, Cupertino"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/api/resolveCoordinates

echo "Demo Fallback to Google Maps API: 201 3rd St num200"
curl -d '{"query":"201 3rd St num200"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/api/resolveCoordinates

echo "Demo Unresolved Address: 11011 Fake Dr. Suite 1001b"
curl -d '{"query":"11011 FakeAddress, Suite 1001b"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/api/resolveCoordinates
