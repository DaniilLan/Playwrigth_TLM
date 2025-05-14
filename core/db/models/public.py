from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, JSON, Text, Time, Interval, \
    Sequence, ARRAY, LargeBinary, SmallInteger
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


# chronic_heart_failure schema models
class ClinicalSign(Base):
    __tablename__ = 'clinical_signs'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class ExaminationRecommendationsGroup(Base):
    __tablename__ = 'examination_recommendations_groups'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, Sequence('examination_recommendations_groups_id_seq'), primary_key=True)
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

    id = Column(Integer, Sequence('examination_recommendations_id_seq'), primary_key=True)
    description = Column(String(200), nullable=False, server_default='')
    group_id = Column(Integer, ForeignKey('chronic_heart_failure.examination_recommendations_groups.id'),
                      nullable=False, server_default='0')

    group = relationship('ExaminationRecommendationsGroup')


class CCRSQuestionnaire(Base):
    __tablename__ = 'ccrs_questionnaires'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
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


class Conclusion(Base):
    __tablename__ = 'conclusions'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, Sequence('conclusions_id_seq'), primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime, nullable=False)
    data = Column(JSON, nullable=False, server_default='{}')


class NYHAFunctionalClass(Base):
    __tablename__ = 'nyha_functional_class'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    functional_class = Column(String(4), nullable=False)


class PatientClinicalSign(Base):
    __tablename__ = 'patients_clinical_signs'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    questionnaire = Column(JSON, server_default='{}')


class PatientExaminationRecommendation(Base):
    __tablename__ = 'patients_examination_recommendations'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, Sequence('patients_examination_recommendations_id_seq'), primary_key=True)
    recommendation_id = Column(Integer, ForeignKey('chronic_heart_failure.examination_recommendations.id'),
                               nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created = Column(DateTime, nullable=False)

    recommendation = relationship('ExaminationRecommendation')
    patient = relationship('User', foreign_keys=[patient_id])


class PatientHeartMurmur(Base):
    __tablename__ = 'patients_heart_murmurs'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, Sequence('patients_heart_murmurs_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    heart_murmur_id = Column(Integer, ForeignKey('chronic_heart_failure.heart_murmurs.id'))

    heart_murmur = relationship('HeartMurmur')
    patient = relationship('User', foreign_keys=[patient_id])


class PatientLifestyleRecommendation(Base):
    __tablename__ = 'patients_lifestyle_recommendations'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    questionnaire = Column(JSON, server_default='{}')


class PatientSymptom(Base):
    __tablename__ = 'patients_symptoms'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    questionnaire = Column(JSON, server_default='{}')


class WellBeingQuestionnaire(Base):
    __tablename__ = 'well_being_questionnaire'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, Sequence('well_being_questionnaire_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'))

    patient = relationship('User', foreign_keys=[patient_id])
    records = relationship('WellBeingRecord', back_populates='questionnaire')


class WellBeingRecord(Base):
    __tablename__ = 'well_being_records'
    __table_args__ = {'schema': 'chronic_heart_failure'}

    id = Column(Integer, Sequence('well_being_records_id_seq'), primary_key=True)
    questionnaire_id = Column(Integer, ForeignKey('chronic_heart_failure.well_being_questionnaire.id'))
    type = Column(String(40))
    value = Column(String(300))

    questionnaire = relationship('WellBeingQuestionnaire', back_populates='records')


# configuration schema models
class Configuration(Base):
    __tablename__ = 'configurations'
    __table_args__ = {'schema': 'configuration'}

    key = Column(String(200), primary_key=True)
    hash = Column(String(500), nullable=False)


# identity schema models
class PhoneCode(Base):
    __tablename__ = 'phones_codes'
    __table_args__ = {'schema': 'identity'}

    id = Column(Integer, Sequence('phones_codes_id_seq'), primary_key=True)
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
    __table_args__ = {'schema': 'identity'}

    id = Column(Integer, Sequence('failed_attempts_id_seq'), primary_key=True)
    ip = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime(timezone=True), nullable=False)

    user = relationship('User', foreign_keys=[user_id])


class PinHash(Base):
    __tablename__ = 'pin_hashes'
    __table_args__ = {'schema': 'identity'}

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    pin_hash = Column(String(200), nullable=False)
    mobile_source_id = Column(String(200), nullable=False, server_default='')


# measurements schema models
class AuscultationNosology(Base):
    __tablename__ = 'auscultation_nosology'
    __table_args__ = {'schema': 'measurements'}

    measurement_id = Column(Integer, ForeignKey('measurements.id'), primary_key=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(30))
    value = Column(String(50))
    annotation = Column(String(300))
    status = Column(String(12), nullable=False)


class ECGAutoConclusion(Base):
    __tablename__ = 'ecg_auto_conclusion'
    __table_args__ = {'schema': 'measurements'}

    measurement_id = Column(Integer, ForeignKey('measurements.id'), primary_key=True)
    created = Column(DateTime, nullable=False)
    value = Column(String(1024))


class ECGSegment(Base):
    __tablename__ = 'ecg_segments'
    __table_args__ = {'schema': 'measurements'}

    measurement_id = Column(Integer, ForeignKey('measurements.id'), primary_key=True)
    segments = Column(JSON)


class PatientMeasurementParameter(Base):
    __tablename__ = 'patients_measurements_parameters'
    __table_args__ = {'schema': 'measurements'}

    patient_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    last_measurement_id = Column(Integer, ForeignKey('measurements.id'))
    measurement_types = Column(ARRAY(String))

    patient = relationship('User', foreign_keys=[patient_id])
    last_measurement = relationship('Measurement', foreign_keys=[last_measurement_id])


# medical schema models
class MedicalTest(Base):
    __tablename__ = 'medical_tests'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('medical_tests_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    display_name = Column(String(50), nullable=False, unique=True)
    created = Column(DateTime, server_default='now()')


class MedicationGroup(Base):
    __tablename__ = 'medications_groups'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('medications_groups_id_seq'), primary_key=True)
    display_name = Column(String(100), nullable=False, server_default='')


class Medication(Base):
    __tablename__ = 'medications'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('medications_id_seq'), primary_key=True)
    display_name = Column(String(60), nullable=False, unique=True)
    recommended_dose = Column(Numeric(8, 4))
    group_id = Column(Integer, ForeignKey('medical.medications_groups.id'))

    group = relationship('MedicationGroup')


class EGFR(Base):
    __tablename__ = 'egfr'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('egfr_id_seq'), primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    value = Column(Numeric(6, 2), nullable=False)
    created = Column(DateTime, nullable=False, server_default='now()')
    method = Column(String(20), nullable=False, server_default='CkdEpi')

    patient = relationship('User', foreign_keys=[patient_id])


class MedicationTaking(Base):
    __tablename__ = 'medications_taking'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('medications_taking_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patients_medications_id = Column(Integer, ForeignKey('medical.patients_medications.id'), nullable=False)
    datetime = Column(DateTime(timezone=True), nullable=False, server_default='now()')

    patient_medication = relationship('PatientMedication', foreign_keys=[patients_medications_id])


class PatientMedicalTest(Base):
    __tablename__ = 'patients_medical_tests'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('medical_tests_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, nullable=False)
    name = Column(String(50), ForeignKey('medical.medical_tests.name'))
    value = Column(String(100), nullable=False)

    patient = relationship('User', foreign_keys=[patient_id])
    test = relationship('MedicalTest', foreign_keys=[name])


class PatientMedicalTestFile(Base):
    __tablename__ = 'patients_medical_tests_files'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('medical_test_files_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(150), nullable=False)
    file = Column(LargeBinary, nullable=False)

    patient = relationship('User', foreign_keys=[patient_id])


class PatientMedication(Base):
    __tablename__ = 'patients_medications'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('patients_medications_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    therapy_id = Column(Integer, ForeignKey('medical.therapies.id'), nullable=False)
    medication_id = Column(Integer, ForeignKey('medical.medications.id'), nullable=False)
    recommended_dose = Column(Numeric(8, 4))
    doctors_comment = Column(String(300))
    deleted = Column(Boolean, nullable=False, server_default='false')
    patients_comment = Column(String(300))
    condition = Column(String(20))

    therapy = relationship('Therapy', foreign_keys=[therapy_id])
    medication = relationship('Medication', foreign_keys=[medication_id])
    taking_times = relationship('TakingTime', back_populates='patient_medication')


class PatientRecommendation(Base):
    __tablename__ = 'patients_recommendations'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('patients_recommendations_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String(50), nullable=False)
    value = Column(String(50), nullable=False)
    deleted = Column(Boolean, nullable=False, server_default='false')

    patient = relationship('User', foreign_keys=[patient_id])


class TakingTime(Base):
    __tablename__ = 'taking_times'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, ForeignKey('medical.patients_medications.id'), primary_key=True)
    taking_time = Column(Time, nullable=False, primary_key=True)

    patient_medication = relationship('PatientMedication', back_populates='taking_times')


class Therapy(Base):
    __tablename__ = 'therapies'
    __table_args__ = {'schema': 'medical'}

    id = Column(Integer, Sequence('therapies_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    updated = Column(DateTime(timezone=True))
    patient_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    completed = Column(Boolean, nullable=False)
    comment = Column(String(500))

    patient = relationship('User', foreign_keys=[patient_id])
    medications = relationship('PatientMedication', back_populates='therapy')


# organization schema models
# class Organization(Base):
#     __tablename__ = 'organizations'
#     __table_args__ = {'schema': 'organization'}
#
#     id = Column(Integer, Sequence('organizations_id_seq'), primary_key=True)
#     created = Column(DateTime, nullable=False)
#     name = Column(String(255))
#     address = Column(String(255))
#     email = Column(String(50))
#     phone = Column(String(10))
#     level = Column(Integer, nullable=False)
#     parent_id = Column(Integer, ForeignKey('organization.organizations.id'))
#     status = Column(String(10))
#
#     parent = relationship('Organization', remote_side=[id])


# patients schema models
class PatientComment(Base):
    __tablename__ = 'patients_comments'
    __table_args__ = {'schema': 'patients'}

    id = Column(Integer, Sequence('patients_comments_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'))
    medworker_id = Column(Integer, ForeignKey('users.id'))
    value = Column(String(255), nullable=False)
    updated = Column(DateTime(timezone=True))
    deleted = Column(Boolean, server_default='false')

    patient = relationship('User', foreign_keys=[patient_id])
    medworker = relationship('User', foreign_keys=[medworker_id])


# public schema models
class AuditEvent(Base):
    __tablename__ = 'audit_events'

    id = Column(Integer, Sequence('audit_events_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    event_type = Column(String(10), nullable=False)
    actor = Column(String(10), nullable=False)
    subject = Column(String(10), nullable=False)
    value = Column(String(200), nullable=False)


class BaseObject(Base):
    __tablename__ = 'base_objects'

    id = Column(Integer, Sequence('base_objects_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(30), nullable=False)
    meta = Column(String(255), nullable=False, server_default='{}')
    source = Column(String(30), nullable=False, server_default='')


class BaseSource(Base):
    __tablename__ = 'base_sources'

    id = Column(Integer, Sequence('base_sources_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(30), nullable=False)
    meta = Column(String(255), nullable=False, server_default='{}')
    source = Column(String(30), nullable=False, server_default='')


class DefaultLimit(Base):
    __tablename__ = 'default_limits'

    id = Column(Integer, Sequence('default_limits_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    min = Column(Numeric(10, 4), nullable=False)
    max = Column(Numeric(10, 4), nullable=False)
    measurement_type = Column(String(255), nullable=False)


class DefaultUserParam(Base):
    __tablename__ = 'default_users_params'

    id = Column(Integer, Sequence('default_users_params_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    type = Column(String(50), nullable=False, unique=True)
    value = Column(String(255), nullable=False)


class Diagnosis(Base):
    __tablename__ = 'diagnoses'

    id = Column(Integer, Sequence('diagnoses_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    code = Column(String(10), nullable=False, unique=True)
    description = Column(String(255), server_default='')


class Role(Base):
    __tablename__ = 'roles'

    created = Column(DateTime, nullable=False)
    role_name = Column(String(30), primary_key=True)


class Treatment(Base):
    __tablename__ = 'treatments'

    id = Column(Integer, Sequence('treatments_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    code = Column(String(10), nullable=False, unique=True)
    description = Column(String(255), server_default='')


class ObjectParam(Base):
    __tablename__ = 'objects_params'

    id = Column(Integer, Sequence('objects_params_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    base_objects_id = Column(Integer, ForeignKey('base_objects.id'))
    type = Column(String(30), nullable=False)
    value = Column(String(255), nullable=False)
    source = Column(String(30), nullable=False, server_default='')

    base_object = relationship('BaseObject')


class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(Integer, Sequence('organizations_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    id_ext = Column(String(50), unique=True)
    name = Column(String(255))
    address = Column(String(255))
    email = Column(String(50), unique=True)
    phone = Column(String(50))
    license = Column(String(255))
    status = Column(String(50))
    parent_id = Column(Integer, ForeignKey('organizations.id'))
    level = Column(Integer, nullable=False, server_default='0')

    parent = relationship('Organization', remote_side=[id])


class SourceParam(Base):
    __tablename__ = 'sources_params'

    id = Column(Integer, Sequence('sources_params_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    base_sources_id = Column(Integer, ForeignKey('base_sources.id'))
    type = Column(String(500), nullable=False)
    value = Column(String(255), nullable=False)
    source = Column(String(30), nullable=False, server_default='')

    base_source = relationship('BaseSource')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    phone = Column(String(20), unique=True)
    phone_trustee = Column(String(20))
    snils = Column(String(20), unique=True)
    org_id = Column(Integer, ForeignKey('organizations.id'))
    first_name = Column(String(50))
    middle_name = Column(String(50))
    last_name = Column(String(50))
    sex = Column(String(10), server_default='male')
    birthdate = Column(DateTime)
    avatar = Column(String(255))
    height = Column(SmallInteger)
    weight = Column(Numeric(10, 2))
    status = Column(String(30), server_default='active')
    password_hash = Column(String(255))
    role_name = Column(String(30), ForeignKey('roles.role_name'), nullable=False)
    deleted = Column(Boolean, nullable=False, server_default='false')
    urgent_inspection = Column(Boolean, server_default='false')

    organization = relationship('Organization', foreign_keys=[org_id])
    role = relationship('Role', foreign_keys=[role_name])


class UserParam(Base):
    __tablename__ = 'users_params'

    id = Column(Integer, Sequence('users_params_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type = Column(String(50), nullable=False)
    value = Column(String(255), nullable=False)
    source = Column(String(30), nullable=False, server_default='')

    user = relationship('User', foreign_keys=[user_id])


class DiagnosisUser(Base):
    __tablename__ = 'diagnoses_users'

    diagnosis_id = Column(Integer, ForeignKey('diagnoses.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    parameters = Column(JSON, server_default='{}')
    id = Column(Integer, Sequence('diagnoses_users_id_seq'), unique=True)
    created = Column(DateTime(timezone=True), server_default='now()')

    diagnosis = relationship('Diagnosis')
    user = relationship('User', foreign_keys=[user_id])


class Form(Base):
    __tablename__ = 'forms'

    id = Column(Integer, Sequence('forms_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_type = Column(String(50), nullable=False)
    answer = Column(String(50), nullable=False)

    user = relationship('User', foreign_keys=[user_id])


class Measurement(Base):
    __tablename__ = 'measurements'

    id = Column(Integer, Sequence('measurements_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String(30), nullable=False)
    type = Column(String(30), nullable=False)
    datetime = Column(DateTime(timezone=True), nullable=False)
    value = Column(String(300), nullable=False)
    deleted = Column(Boolean, nullable=False, server_default='false')
    need_inspection = Column(Boolean, nullable=False, server_default='false')
    norm = Column(String(20), nullable=False)

    user = relationship('User', foreign_keys=[user_id])
    params = relationship('MeasurementParam', back_populates='measurement')


class MeasurementComment(Base):
    __tablename__ = 'measurements_comments'

    id = Column(Integer, Sequence('measurements_comments_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    value = Column(String(700), nullable=False)
    updated = Column(DateTime)

    user = relationship('User', foreign_keys=[user_id])
    measurement = relationship('Measurement', foreign_keys=[measurement_id])


class MeasurementLimit(Base):
    __tablename__ = 'measurements_limits'

    id = Column(Integer, Sequence('measurements_limits_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    min = Column(Numeric(10, 4), nullable=False)
    max = Column(Numeric(10, 4), nullable=False)
    measurement_type = Column(String(255), nullable=False)
    patient_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    patient = relationship('User', foreign_keys=[patient_id])


class MeasurementTracking(Base):
    __tablename__ = 'measurements_tracking'

    id = Column(Integer, Sequence('measurements_tracking_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    initiator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    initiator_org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    measurement_id = Column(Integer, ForeignKey('measurements.id'))

    initiator = relationship('User', foreign_keys=[initiator_id])
    initiator_org = relationship('Organization', foreign_keys=[initiator_org_id])
    measurement = relationship('Measurement', foreign_keys=[measurement_id])


class MedicalInformation(Base):
    __tablename__ = 'medical_informations'

    id = Column(Integer, Sequence('medical_informations_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    corporate_health = Column(Boolean)
    top_pressure = Column(Numeric(10, 2))
    low_pressure = Column(Numeric(10, 2))

    user = relationship('User', foreign_keys=[user_id])


class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, Sequence('notifications_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    is_read = Column(Boolean, nullable=False, server_default='false')
    recipient_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String(500), nullable=False)
    deleted = Column(Boolean, nullable=False, server_default='false')
    title = Column(String(50), nullable=False, server_default='')
    type = Column(String(50), nullable=False, server_default='')

    recipient = relationship('User', foreign_keys=[recipient_id])


class RecoveredPassword(Base):
    __tablename__ = 'recovered_passwords'

    id = Column(Integer, Sequence('recovered_passwords_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    expiration_time = Column(DateTime, nullable=False)

    user = relationship('User', foreign_keys=[user_id])


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, Sequence('subscriptions_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    publisher_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    subscriber_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    event_type = Column(String(50), nullable=False)
    subscribed = Column(Boolean, nullable=False, server_default='true')

    publisher = relationship('User', foreign_keys=[publisher_id])
    subscriber = relationship('User', foreign_keys=[subscriber_id])


class TreatmentUser(Base):
    __tablename__ = 'treatments_users'

    treatment_id = Column(Integer, ForeignKey('treatments.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    treatment = relationship('Treatment')
    user = relationship('User', foreign_keys=[user_id])


class UrgentInspection(Base):
    __tablename__ = 'urgent_inspections'

    id = Column(Integer, Sequence('urgent_inspections_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    initiator_id = Column(Integer, ForeignKey('users.id'))
    patient_id = Column(Integer, ForeignKey('users.id'))
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    action = Column(String(10), nullable=False)

    initiator = relationship('User', foreign_keys=[initiator_id])
    patient = relationship('User', foreign_keys=[patient_id])
    measurement = relationship('Measurement', foreign_keys=[measurement_id])


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, Sequence('user_info_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comment = Column(Text)

    user = relationship('User', foreign_keys=[user_id])

class ECGConclusion(Base):
    __tablename__ = 'ecg_conclusions'

    id = Column(Integer, Sequence('ecg_conclusions_id_seq'), primary_key=True)
    value = Column(String(1000), nullable=False)
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    measurement = relationship('Measurement', foreign_keys=[measurement_id])
    user = relationship('User', foreign_keys=[user_id])


class MeasurementParam(Base):
    __tablename__ = 'measurement_params'

    id = Column(Integer, Sequence('measurement_params_id_seq'), primary_key=True)
    created = Column(DateTime, nullable=False)
    measurement_id = Column(Integer, ForeignKey('measurements.id'))
    type = Column(String(30), nullable=False)
    value = Column(String(255), nullable=False)

    measurement = relationship('Measurement', foreign_keys=[measurement_id])


# tech schema models
class DBVersion(Base):
    __tablename__ = 'dbversions'
    __table_args__ = {'schema': 'tech'}

    Scope = Column(String(128), primary_key=True)
    Version = Column(Integer, nullable=False)


# vks schema models
class MeetingUser(Base):
    __tablename__ = 'meeting_user'
    __table_args__ = {'schema': 'vks'}

    meeting_id = Column(Integer, ForeignKey('vks.meetings.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    meeting = relationship('Meeting', foreign_keys=[meeting_id])
    user = relationship('User', foreign_keys=[user_id])


class Meeting(Base):
    __tablename__ = 'meetings'
    __table_args__ = {'schema': 'vks'}

    id = Column(Integer, Sequence('meetings_id_seq'), primary_key=True)
    created = Column(DateTime(timezone=True), server_default='now()')
    updated = Column(DateTime(timezone=True), server_default='now()')
    room_id = Column(String(50), nullable=False, unique=True)
    initiator_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(50))
    description = Column(String(255))
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    deleted = Column(Boolean)
    dates_offset = Column(Interval)

    initiator = relationship('User', foreign_keys=[initiator_id])
    participants = relationship('User', secondary='vks.meeting_user', viewonly=True)