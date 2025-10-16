import qarnot
import dotenv
import os 

dotenv.load_dotenv()

conn = qarnot.connection.Connection(client_token=os.getenv("QARNOT_API_KEY"))

nb_mpi = 28

task = conn.create_task("code-saturne demo", 'code-saturne', 1)
task.constants['WORKING_DIRECTORY'] ='/job'
task.constants['SETUP_CLUSTER_NB_SLOTS'] = '28'
task.constants['CS_CASE_DIR'] = 'Blade'
task.constants['LOG_FREQUENCY'] = "30"
task.constants['CS_MPI_NBPROC'] = f"{nb_mpi}"
task.constants['SETUP_CLUSTER_MPIHOST_STYLE'] = "colon"

task.hardware_constraints = [
    qarnot.hardware_constraint.SpecificHardware('28c-128g-intel-dual-xeon2680v4-ssd')
]

input_bucket = conn.create_bucket("cs-public-case")
input_bucket.add_directory("Blade", "Blade")

task.resources.append(input_bucket)
task.results = input_bucket
task.submit()
