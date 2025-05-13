from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Date, Numeric,
    ForeignKey, Index, CheckConstraint, UniqueConstraint, JSON, Interval, func, Time, LargeBinary, ARRAY
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


# Модели для схемы chronic_heart_failure
class ClinicalSign(Base):
    __tablename__ = 'clinical_signs'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class ExaminationRecommendationsGroup(Base):
    __tablename__ = 'examination_recommendations_groups'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    display_name = Column(String(100), nullable=False)


class HeartMurmur(Base):
    __tablename__ = 'heart_murmurs'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False, unique=True)


class LifestyleRecommendation(Base):
    __tablename__ = 'lifestyle_recommendations'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Symptom(Base):
    __tablename__ = 'symptoms'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class ExaminationRecommendation(Base):
    __tablename__ = 'examination_recommendations'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(200), nullable=False, server_default='')
    group_id = Column(Integer, ForeignKey('chronic_heart_failure.examination_recommendations_groups.id'),
                      nullable=False, server_default='0')

    group = relationship("ExaminationRecommendationsGroup")


class CCRSQuestionnaire(Base):
    __tablename__ = 'ccrs_questionnaires'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    functional_class = Column(String(4), nullable=False)
    dyspnea = Column(String(20), nullable=False)
    weight_change = Column(String(20), nullable=False)
    heart_complaint = Column(String(20), nullable=False)
    lying_position = Column(String(20), nullable=False)
    swollen_neck_veins = Column(String(20), nullable=False)
    wheezing = Column(String(20), nullable=False)
    gallop_rhythm = Column(String(20), nullable=False)
    liver = Column(String(20), nullable=False)
    edema = Column(String(20), nullable=False)
    systolic = Column(String(20), nullable=False)

    user = relationship("User")


class Conclusion(Base):
    __tablename__ = 'conclusions'
    __table_args__ = (
        {'schema': 'chronic_heart_failure'},
        Index('idx_conclusions_patient_id_created', 'patient_id', 'created')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('public.users.id'))
    created = Column(DateTime, nullable=False)
    data = Column(JSONB, nullable=False, server_default='{}')

    patient = relationship("User")


class NYHAFunctionalClass(Base):
    __tablename__ = 'nyha_functional_class'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)
    functional_class = Column(String(4), nullable=False)

    user = relationship("User")


class PatientsClinicalSign(Base):
    __tablename__ = 'patients_clinical_signs'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)
    questionnaire = Column(JSONB, server_default='{}')

    user = relationship("User")


class PatientsExaminationRecommendation(Base):
    __tablename__ = 'patients_examination_recommendations'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    recommendation_id = Column(Integer,
                               ForeignKey('chronic_heart_failure.examination_recommendations.id'),
                               nullable=False)
    patient_id = Column(Integer, ForeignKey('public.users.id'), nullable=False)
    created = Column(DateTime, nullable=False)

    recommendation = relationship("ExaminationRecommendation")
    patient = relationship("User")


class PatientsHeartMurmur(Base):
    __tablename__ = 'patients_heart_murmurs'
    __table_args__ = (
        {'schema': 'chronic_heart_failure'},
        Index('idx_patients_heart_murmurs_patient_id', 'patient_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    patient_id = Column(Integer, ForeignKey('public.users.id'), nullable=False)
    heart_murmur_id = Column(Integer, ForeignKey('chronic_heart_failure.heart_murmurs.id'))

    patient = relationship("User")
    heart_murmur = relationship("HeartMurmur")


class PatientsLifestyleRecommendation(Base):
    __tablename__ = 'patients_lifestyle_recommendations'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)
    questionnaire = Column(JSONB, server_default='{}')

    user = relationship("User")


class PatientsSymptom(Base):
    __tablename__ = 'patients_symptoms'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)
    questionnaire = Column(JSONB, server_default='{}')

    user = relationship("User")


class WellBeingQuestionnaire(Base):
    __tablename__ = 'well_being_questionnaire'
    __table_args__ = (
        {'schema': 'chronic_heart_failure'},
        Index('idx_well_being_questionnaire_patientid', 'patient_id'),
        Index('idx_well_being_questionnaire_patientid_created', 'patient_id', 'created')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('public.users.id'))

    patient = relationship("User")


class WellBeingRecord(Base):
    __tablename__ = 'well_being_records'
    __table_args__ = (
        {'schema': 'chronic_heart_failure'},
        Index('idx_well_being_records_questionnaire_id', 'questionnaire_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    questionnaire_id = Column(Integer, ForeignKey('chronic_heart_failure.well_being_questionnaire.id'))
    type = Column(String(40))
    value = Column(String(300))

    questionnaire = relationship("WellBeingQuestionnaire")


# Модели для схемы configuration
class Configuration(Base):
    __tablename__ = 'configurations'
    __table_args__ = {'schema': 'configuration'}

    key = Column(String(200), primary_key=True)
    hash = Column(String(500), nullable=False)


# Модели для схемы identity
class PhoneCode(Base):
    __tablename__ = 'phones_codes'
    __table_args__ = (
        {'schema': 'identity'},
        Index('idx_phones_codes_phone', 'phone', postgresql_using='hash')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    code_hash = Column(String(40), nullable=False)


class Source(Base):
    __tablename__ = 'sources'
    __table_args__ = {'schema': 'identity'}

    created = Column(DateTime, nullable=False)
    id = Column(String(255), primary_key=True)


class FailedAttempt(Base):
    __tablename__ = 'failed_attempts'
    __table_args__ = (
        {'schema': 'identity'},
        Index('idx_failed_attempts_ip_created', 'ip', 'created'),
        Index('idx_failed_attempts_user_id_created', 'user_id', 'created')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('public.users.id'))
    created = Column(DateTime(timezone=True), nullable=False)

    user = relationship("User")


class PinHash(Base):
    __tablename__ = 'pin_hashes'
    __table_args__ = {'schema': 'identity'}

    id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    pin_hash = Column(String(200), nullable=False)
    mobile_source_id = Column(String(200), nullable=False, server_default='')

    user = relationship("User")


# Модели для схемы measurements
class AuscultationNosology(Base):
    __tablename__ = 'auscultation_nosology'
    __table_args__ = {'schema': 'measurements'}

    measurement_id = Column(Integer, ForeignKey('public.measurements.id'), primary_key=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(30))
    value = Column(String(50))
    annotation = Column(String(300))
    status = Column(String(12), nullable=False)

    measurement = relationship("Measurement")


class ECGAutoConclusion(Base):
    __tablename__ = 'ecg_auto_conclusion'
    __table_args__ = {'schema': 'measurements'}

    measurement_id = Column(Integer, ForeignKey('public.measurements.id'), primary_key=True)
    created = Column(DateTime, nullable=False)
    value = Column(String(1024))

    measurement = relationship("Measurement")


class ECGSegment(Base):
    __tablename__ = 'ecg_segments'
    __table_args__ = (
        {'schema': 'measurements'},
        Index('idx_ecg_segments_measurement_id', 'measurement_id', postgresql_using='hash')
    )

    measurement_id = Column(Integer, ForeignKey('public.measurements.id'), primary_key=True)
    segments = Column(JSONB)

    measurement = relationship("Measurement")


class PatientMeasurementParameter(Base):
    __tablename__ = 'patients_measurements_parameters'
    __table_args__ = (
        {'schema': 'measurements'},
        Index('idx_patients_measurements_parameter_patient_id', 'patient_id', postgresql_using='hash')
    )

    patient_id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)
    last_measurement_id = Column(Integer, ForeignKey('public.measurements.id'))
    measurement_types = Column(ARRAY(String))

    patient = relationship("User")
    last_measurement = relationship("Measurement")


# Модели для схемы medical
class MedicalTest(Base):
    __tablename__ = 'medical_tests'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    display_name = Column(String(50), nullable=False, unique=True)
    created = Column(DateTime, server_default=func.now())


class MedicationsGroup(Base):
    __tablename__ = 'medications_groups'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    display_name = Column(String(100), nullable=False, server_default='')


class Medication(Base):
    __tablename__ = 'medications'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_medications_display_name', 'display_name')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    display_name = Column(String(60), nullable=False, unique=True)
    recommended_dose = Column(Numeric(8, 4))
    group_id = Column(Integer, ForeignKey('medical.medications_groups.id'))

    group = relationship("MedicationsGroup")


class EGFR(Base):
    __tablename__ = 'egfr'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_egfr_patient_id', 'patient_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('public.users.id'), nullable=False, unique=True)
    value = Column(Numeric(6, 2), nullable=False)
    created = Column(DateTime, nullable=False, server_default=func.now())
    method = Column(String(20), nullable=False, server_default='CkdEpi')

    patient = relationship("User")


class MedicationsTaking(Base):
    __tablename__ = 'medications_taking'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_medications_taking_patients_medications_id', 'patients_medications_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patients_medications_id = Column(Integer, ForeignKey('medical.patients_medications.id'), nullable=False)
    datetime = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    patient_medication = relationship("PatientMedication")


class PatientMedicalTest(Base):
    __tablename__ = 'patients_medical_tests'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_medical_tests_patientid_created', 'patient_id', 'created'),
        Index('idx_medical_tests_patientid_name', 'patient_id', 'name')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False)
    patient_id = Column(Integer, ForeignKey('public.users.id'))
    date = Column(DateTime, nullable=False)
    name = Column(String(50), ForeignKey('medical.medical_tests.name'))
    value = Column(String(100), nullable=False)

    patient = relationship("User")
    test = relationship("MedicalTest")


class PatientMedicalTestFile(Base):
    __tablename__ = 'patients_medical_tests_files'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_medical_test_files_patientid_created', 'patient_id', 'created')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('public.users.id'))
    name = Column(String(150), nullable=False)
    file = Column(LargeBinary, nullable=False)

    patient = relationship("User")


class PatientMedication(Base):
    __tablename__ = 'patients_medications'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_patients_medications_therapy_id_medication_id', 'therapy_id', 'medication_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    therapy_id = Column(Integer, ForeignKey('medical.therapies.id'), nullable=False)
    medication_id = Column(Integer, ForeignKey('medical.medications.id'), nullable=False)
    recommended_dose = Column(Numeric(8, 4))
    doctors_comment = Column(String(300))
    deleted = Column(Boolean, nullable=False, server_default='false')
    patients_comment = Column(String(300))
    condition = Column(String(20))

    therapy = relationship("Therapy")
    medication = relationship("Medication")


class PatientRecommendation(Base):
    __tablename__ = 'patients_recommendations'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_patients_recommendations_patient_id_type', 'patient_id', 'type')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('public.users.id'))
    type = Column(String(50), nullable=False)
    value = Column(String(50), nullable=False)
    deleted = Column(Boolean, nullable=False, server_default='false')

    patient = relationship("User")


class TakingTime(Base):
    __tablename__ = 'taking_times'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_taking_times_id', 'id')
    )

    id = Column(Integer, ForeignKey('medical.patients_medications.id'), primary_key=True)
    taking_time = Column(Time, primary_key=True)

    patient_medication = relationship("PatientMedication")


class Therapy(Base):
    __tablename__ = 'therapies'
    __table_args__ = (
        {'schema': 'medical'},
        Index('idx_therapies_patient_id', 'patient_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    updated = Column(DateTime(timezone=True))
    patient_id = Column(Integer, ForeignKey('public.users.id'), nullable=False)
    completed = Column(Boolean, nullable=False)
    comment = Column(String(500))

    patient = relationship("User")


# # Модели для схемы organization
# class Organization(Base):
#     __tablename__ = 'organizations'
#     __table_args__ = (
#         {'schema': 'organization'},
#         Index('idx_organization_organizations_id', 'id', postgresql_using='hash')
#     )
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     created = Column(DateTime, nullable=False)
#     name = Column(String(255))
#     address = Column(String(255))
#     email = Column(String(50), unique=True)
#     phone = Column(String(10))
#     level = Column(Integer, nullable=False)
#     parent_id = Column(Integer, ForeignKey('organization.organizations.id'))
#     status = Column(String(10))
#
#     parent = relationship("Organization", remote_side=[id])


# Модели для схемы patients
class PatientComment(Base):
    __tablename__ = 'patients_comments'
    __table_args__ = (
        {'schema': 'patients'},
        Index('idx_patients_comments_medworker_id', 'medworker_id'),
        Index('idx_patients_comments_patient_id', 'patient_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('public.users.id'))
    medworker_id = Column(Integer, ForeignKey('public.users.id'))
    value = Column(String(255), nullable=False)
    updated = Column(DateTime(timezone=True))
    deleted = Column(Boolean, server_default='false')

    patient = relationship("User", foreign_keys=[patient_id])
    medworker = relationship("User", foreign_keys=[medworker_id])


# Модели для схемы tech
class DBVersion(Base):
    __tablename__ = 'dbversions'
    __table_args__ = {'schema': 'tech'}

    Scope = Column(String(128), primary_key=True)
    Version = Column(Integer, nullable=False)


# Модели для схемы vks
class MeetingUser(Base):
    __tablename__ = 'meeting_user'
    __table_args__ = (
        {'schema': 'vks'},
        Index('idx_vks_meeting_user_meeting_id', 'meeting_id'),
        Index('idx_vks_meeting_user_user_id', 'user_id')
    )

    meeting_id = Column(Integer, ForeignKey('vks.meetings.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('public.users.id'), primary_key=True)

    meeting = relationship("Meeting")
    user = relationship("User")


class Meeting(Base):
    __tablename__ = 'meetings'
    __table_args__ = (
        {'schema': 'vks'},
        Index('idx_vks_meetings_initiator_id', 'initiator_id')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now())
    room_id = Column(String(50), nullable=False, unique=True)
    initiator_id = Column(Integer, ForeignKey('public.users.id'))
    name = Column(String(50))
    description = Column(String(255))
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    deleted = Column(Boolean)
    dates_offset = Column(Interval)

    initiator = relationship("User")
    participants = relationship("User", secondary="vks.meeting_user")


