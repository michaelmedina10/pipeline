build:
	docker build . -t pipeline

run:
	docker run -p8000:8000 --name pipeline pipeline

remove:
	docker rm -f pipeline

exec:
	make remove || true
	make build
	make run
