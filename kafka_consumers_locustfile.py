"""
Load test for kafka consumer
"""
from locust import Locust

from infrastructure import (
    full_path_from_module_relative_path,
    create_locust_class,
)
from infrastructure.kafka import KafkaProducerMixin, Outcome
from tasks.kafka_tasks import (
    kafka_outcome_task,
    kafka_random_outcome_task,
    kafka_configurable_outcome_task_factory,
    random_kafka_event_task_factory,
)

accepted_outcome = kafka_outcome_task(Outcome.ACCEPTED)
rate_limited_outcome = kafka_outcome_task(Outcome.RATE_LIMITED)
random_outcome = kafka_random_outcome_task
kafka_configurable_outcome_factory = kafka_configurable_outcome_task_factory
random_kafka_event_task_factory = random_kafka_event_task_factory

_config_path = full_path_from_module_relative_path(
    __file__, "config/kafka_consumers.test.yml"
)
Outcomes = create_locust_class(
    "Outcomes", _config_path, __name__, base_classes=(Locust, KafkaProducerMixin)
)
Events = create_locust_class(
    "Events", _config_path, __name__, base_classes=(Locust, KafkaProducerMixin)
)
