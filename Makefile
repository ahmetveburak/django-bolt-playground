run:
	uv run python manage.py runbolt --dev

dev:
	@echo "Starting backend and frontend servers..."
	@trap 'kill 0' EXIT; \
	uv run python manage.py runbolt --dev & \
	cd frontend && npm run dev & \
	wait