from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Date, Numeric,
    ForeignKey, Index, CheckConstraint, UniqueConstraint, JSON
)


Base = declarative_base()

class AuditEvent(Base):
    __tablename__ = 'audit_events'
    __table_args__ = (
        UniqueConstraint('id', name='audit_events_id_key'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    event_type = Column(String(10), nullable=False)
    actor = Column(String(10), nullable=False)
    subject = Column(String(10), nullable=False)
    value = Column(String(200), nullable=False)

class BaseObject(Base):
    __tablename__ = 'base_objects'
    __table_args__ = (
        UniqueConstraint('id', name='base_objects_id_key'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(30), nullable=False)
    meta = Column(String(255), nullable=False, server_default='{}')
    source = Column(String(30), nullable=False, server_default='')

class BaseSource(Base):
    __tablename__ = 'base_sources'
    __table_args__ = (
        UniqueConstraint('id', name='base_sources_id_key'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(30), nullable=False)
    meta = Column(String(255), nullable=False, server_default='{}')
    source = Column(String(30), nullable=False, server_default='')

class DefaultLimit(Base):
    __tablename__ = 'default_limits'
    __table_args__ = (
        UniqueConstraint('id', name='default_limits_id_key'),
        Index('idx_default_limits_measurement_type', 'measurement_type'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    min = Column(Numeric(10, 4), nullable=False)
    max = Column(Numeric(10, 4), nullable=False)
    measurement_type = Column(String(255), nullable=False)

class DefaultUserParam(Base):
    __tablename__ = 'default_users_params'
    __table_args__ = (
        UniqueConstraint('id', name='default_users_params_id_key'),
        UniqueConstraint('type', name='default_users_params_type_key'),
        Index('idx_default_userss_params_type', 'type'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(50), nullable=False)
    value = Column(String(255), nullable=False)

class Diagnosis(Base):
    __tablename__ = 'diagnoses'
    __table_args__ = (
        UniqueConstraint('id', name='diagnoses_id_key'),
        UniqueConstraint('code', name='diagnoses_code_key'),
        Index('idx_diagnoses_code', 'code'),
        Index('idx_diagnoses_id', 'id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    code = Column(String(10), nullable=False)
    description = Column(String(255))

class Role(Base):
    __tablename__ = 'roles'
    __table_args__ = (
        UniqueConstraint('role_name', name='roles_role_name_key'),
    )

    created = Column(DateTime, nullable=False)
    role_name = Column(String(30), primary_key=True)

class Treatment(Base):
    __tablename__ = 'treatments'
    __table_args__ = (
        UniqueConstraint('id', name='treatments_id_key'),
        UniqueConstraint('code', name='treatments_code_key'),
        Index('idx_treatments_code', 'code'),
        Index('idx_treatments_id', 'id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    code = Column(String(10), nullable=False)
    description = Column(String(255))

class ObjectParam(Base):
    __tablename__ = 'objects_params'
    __table_args__ = (
        UniqueConstraint('id', name='objects_params_id_key'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    base_objects_id = Column(Integer, ForeignKey('base_objects.id'))
    type = Column(String(30), nullable=False)
    value = Column(String(255), nullable=False)
    source = Column(String(30), nullable=False, server_default='')

    base_object = relationship("BaseObject")

class Organization(Base):
    __tablename__ = 'organizations'
    __table_args__ = (
        UniqueConstraint('id', name='organizations_id_key'),
        UniqueConstraint('id_ext', name='organizations_id_ext_key'),
        UniqueConstraint('email', name='organizations_email_key'),
        Index('idx_organizations_id', 'id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    id_ext = Column(String(50))
    name = Column(String(255))
    address = Column(String(255))
    email = Column(String(50))
    phone = Column(String(50))
    license = Column(String(255))
    status = Column(String(50))
    parent_id = Column(Integer, ForeignKey('organizations.id'))
    level = Column(Integer, nullable=False, server_default='0')

    parent = relationship("Organization", remote_side=[id])

class SourceParam(Base):
    __tablename__ = 'sources_params'
    __table_args__ = (
        UniqueConstraint('id', name='sources_params_id_key'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    base_sources_id = Column(Integer, ForeignKey('base_sources.id'))
    type = Column(String(500), nullable=False)
    value = Column(String(255), nullable=False)
    source = Column(String(30), nullable=False, server_default='')

    base_source = relationship("BaseSource")

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('id', name='users_id_key'),
        UniqueConstraint('username', name='users_username_key'),
        UniqueConstraint('email', name='users_email_key'),
        UniqueConstraint('phone', name='users_phone_key'),
        UniqueConstraint('snils', name='users_snils_key'),
        Index('idx_users_email', 'email'),
        Index('idx_users_id', 'id'),
        Index('idx_users_org_id', 'org_id'),
        Index('idx_users_role_name', 'role_name'),
        CheckConstraint("sex IN ('male', 'female', 'other')", name='ck_user_sex'),
        CheckConstraint("status IN ('active', 'inactive', 'banned')", name='ck_user_status'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    username = Column(String(50))
    email = Column(String(50))
    phone = Column(String(20))
    phone_trustee = Column(String(20))
    snils = Column(String(20))
    org_id = Column(Integer, ForeignKey('organizations.id'))
    first_name = Column(String(50))
    middle_name = Column(String(50))
    last_name = Column(String(50))
    sex = Column(String(10), server_default='male')
    birthdate = Column(DateTime)
    avatar = Column(String(255))
    height = Column(Integer)
    weight = Column(Numeric(10, 2))
    status = Column(String(30), server_default='active')
    password_hash = Column(String(255))
    role_name = Column(String(30), ForeignKey('roles.role_name'), nullable=False)
    deleted = Column(Boolean, server_default='false')
    urgent_inspection = Column(Boolean)

    organization = relationship("Organization")
    role = relationship("Role")

class UserParam(Base):
    __tablename__ = 'users_params'
    __table_args__ = (
        UniqueConstraint('id', name='users_params_id_key'),
        Index('idx_users_params_type', 'type'),
        Index('idx_users_params_user_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type = Column(String(50), nullable=False)
    value = Column(String(255), nullable=False)
    source = Column(String(30), nullable=False, server_default='')

    user = relationship("User")

class DiagnosisUser(Base):
    __tablename__ = 'diagnoses_users'
    __table_args__ = (
        UniqueConstraint('id', name='diagnoses_users_id_key'),
        UniqueConstraint('diagnosis_id', 'user_id', name='diagnoses_users_diagnosis_id_user_id_key'),
        Index('idx_diagnoses_users_diagnosis_id', 'diagnosis_id'),
        Index('idx_diagnoses_users_user_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    diagnosis_id = Column(Integer, ForeignKey('diagnoses.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    parameters = Column(JSON, server_default='{}')
    created = Column(DateTime, server_default='now()')

    diagnosis = relationship("Diagnosis")
    user = relationship("User")

class Form(Base):
    __tablename__ = 'forms'
    __table_args__ = (
        UniqueConstraint('id', name='forms_id_key'),
        Index('idx_forms_id', 'id'),
        Index('idx_forms_user_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_type = Column(String(50), nullable=False)
    answer = Column(String(50), nullable=False)

    user = relationship("User")

class Measurement(Base):
    __tablename__ = 'measurements'
    __table_args__ = (
        UniqueConstraint('id', name='measurements_id_key'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String(30), nullable=False)
    type = Column(String(30), nullable=False)
    datetime = Column(DateTime, nullable=False)
    value = Column(String(300), nullable=False)
    deleted = Column(Boolean, server_default='false')
    need_inspection = Column(Boolean, server_default='false')
    norm = Column(String(20), nullable=False)

    user = relationship("User")

class MeasurementComment(Base):
    __tablename__ = 'measurements_comments'
    __table_args__ = (
        UniqueConstraint('id', name='measurements_comments_id_key'),
        Index('idx_measurements_comments_id', 'id'),
        Index('idx_measurements_comments_measurement_id', 'measurement_id'),
        Index('idx_measurements_comments_user_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    value = Column(String(700), nullable=False)
    updated = Column(DateTime)

    user = relationship("User")
    measurement = relationship("Measurement")

class MeasurementLimit(Base):
    __tablename__ = 'measurements_limits'
    __table_args__ = (
        UniqueConstraint('id', name='measurements_limits_id_key'),
        UniqueConstraint('measurement_type', 'patient_id', name='measurements_limits_measurement_type_patient_id'),
        Index('idx_measurements_limits_id', 'id', postgresql_using='hash'),
        Index('idx_measurements_limits_measurement_type', 'measurement_type'),
        Index('idx_measurements_limits_patient_id_measurement_type', 'patient_id', 'measurement_type'),
        Index('idx_measurements_limits_user_id', 'patient_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    min = Column(Numeric(10, 4), nullable=False)
    max = Column(Numeric(10, 4), nullable=False)
    measurement_type = Column(String(255), nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    patient = relationship("User")

class MeasurementTracking(Base):
    __tablename__ = 'measurements_tracking'
    __table_args__ = (
        UniqueConstraint('id', name='measurements_tracking_id_key'),
        Index('idx_measurements_tracking_initiator_id', 'initiator_id'),
        Index('idx_measurements_tracking_initiator_org_id', 'initiator_org_id'),
        Index('idx_measurements_tracking_measurement_id', 'measurement_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    initiator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    initiator_org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    measurement_id = Column(Integer, ForeignKey('measurements.id'))

    initiator = relationship("User", foreign_keys=[initiator_id])
    initiator_org = relationship("Organization")
    measurement = relationship("Measurement")

class MedicalInformation(Base):
    __tablename__ = 'medical_informations'
    __table_args__ = (
        UniqueConstraint('id', name='medical_informations_id_key'),
        UniqueConstraint('user_id', name='medical_informations_user_id_key'),
        Index('idx_medical_informations_id', 'id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    corporate_health = Column(Boolean)
    top_pressure = Column(Numeric(10, 2))
    low_pressure = Column(Numeric(10, 2))

    user = relationship("User")

class Notification(Base):
    __tablename__ = 'notifications'
    __table_args__ = (
        UniqueConstraint('id', name='notifications_id_key'),
        Index('idx_notifications_id', 'id'),
        Index('idx_notifications_recipient_id', 'recipient_id'),
        Index('idx_notifications_type', 'type'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    is_read = Column(Boolean, server_default='false')
    recipient_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String(500), nullable=False)
    deleted = Column(Boolean, server_default='false')
    title = Column(String(50), server_default='')
    type = Column(String(50), server_default='')

    recipient = relationship("User")

class RecoveredPassword(Base):
    __tablename__ = 'recovered_passwords'
    __table_args__ = (
        UniqueConstraint('id', name='recovered_passwords_id_key'),
        UniqueConstraint('user_id', name='recovered_passwords_user_id_key'),
        Index('idx_recovered_passwords_user_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    password_hash = Column(String(255), nullable=False)
    expiration_time = Column(DateTime, nullable=False)

    user = relationship("User")

class Subscription(Base):
    __tablename__ = 'subscriptions'
    __table_args__ = (
        UniqueConstraint('id', name='subscriptions_id_key'),
        Index('idx_subscriptions_event_type', 'event_type'),
        Index('idx_subscriptions_publisher_id', 'publisher_id'),
        Index('idx_subscriptions_subscriber_id', 'subscriber_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    publisher_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    subscriber_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    event_type = Column(String(50), nullable=False)
    subscribed = Column(Boolean, server_default='true')

    publisher = relationship("User", foreign_keys=[publisher_id])
    subscriber = relationship("User", foreign_keys=[subscriber_id])

class TreatmentUser(Base):
    __tablename__ = 'treatments_users'
    __table_args__ = (
        Index('idx_treatments_users_treatment_id', 'treatment_id'),
        Index('idx_treatments_users_user_id', 'user_id'),
    )

    treatment_id = Column(Integer, ForeignKey('treatments.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    treatment = relationship("Treatment")
    user = relationship("User")

class UrgentInspection(Base):
    __tablename__ = 'urgent_inspections'
    __table_args__ = (
        UniqueConstraint('id', name='urgent_inspections_id_key'),
        Index('idx_urgent_inspections_id', 'id'),
        Index('idx_urgent_inspections_initiator_id', 'initiator_id'),
        Index('idx_urgent_inspections_measurement_id', 'measurement_id'),
        Index('idx_urgent_inspections_patient_id', 'patient_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    initiator_id = Column(Integer, ForeignKey('users.id'))
    patient_id = Column(Integer, ForeignKey('users.id'))
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    action = Column(String(10), nullable=False)

    initiator = relationship("User", foreign_keys=[initiator_id])
    patient = relationship("User", foreign_keys=[patient_id])
    measurement = relationship("Measurement")

class UserInfo(Base):
    __tablename__ = 'user_info'
    __table_args__ = (
        UniqueConstraint('id', name='user_info_id_key'),
        Index('idx_user_info_id', 'id'),
        Index('idx_user_info_user_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comment = Column(String)

    user = relationship("User")

class ECGConclusion(Base):
    __tablename__ = 'ecg_conclusions'
    __table_args__ = (
        UniqueConstraint('id', name='ecg_conclusions_id_key'),
        Index('idx_ecg_conclusions_id', 'id'),
        Index('idx_ecg_conclusions_measurement_id', 'measurement_id'),
        Index('idx_ecg_conclusions_user_id', 'user_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(1000), nullable=False)
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    measurement = relationship("Measurement")
    user = relationship("User")

class MeasurementParam(Base):
    __tablename__ = 'measurement_params'
    __table_args__ = (
        UniqueConstraint('id', name='measurement_params_id_key'),
        UniqueConstraint('measurement_id', 'type', name='measurement_params_measurement_id_type_key'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    type = Column(String(30), nullable=False)
    value = Column(String(255), nullable=False)

    measurement = relationship("Measurement")


