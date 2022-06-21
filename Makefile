.DEFAULT_GOAL := help
DOCKER_PROD = docker-compose.yml
UGC_STACK_NAME = "notificarion"
#####---PROD---#####
help:
	$(info ------------------------------------------------------------------------------------------------------------------------------)
	$(info "#####---PROD---#####" (build, up, build_up, start, down, destroy, stop, restart))
	$(info ------------------------------------------------------------------------------------------------------------------------------)
build:
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} build
up:
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} up -d
build_up: build up
start:
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} start
down:
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} down
destroy:
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} down -v
	docker volume ls -f dangling=true
	docker volume prune --force
	docker image prune --force --filter="dangling=true"
stop:
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} stop
restart:
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} stop
	docker-compose -p ${UGC_STACK_NAME} -f ${DOCKER_PROD} up -d
