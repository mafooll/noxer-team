.PHONY: run migrate upgrade initial shell psql-shell cleanup

include .env
export

run:
	docker-compose up

initial:
	docker-compose run --rm web uv run flask db init
	docker-compose run --rm web uv run flask db migrate -m "initial"
	docker-compose run --rm web uv run flask db upgrade
	docker-compose up

migrate:
	docker-compose run --rm web uv run flask db migrate -m "$(msg)"

upgrade:
	docker-compose run --rm web uv run flask db upgrade

shell:
	docker-compose run --rm web sh

psql-shell:
	docker exec -it noxer-team-db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

cleanup:
	docker-compose down -v --remove-orphans
