#!/bin/bash
echo "Running integration tests..."
pytest api/tests

chmod +x tests/integration.sh