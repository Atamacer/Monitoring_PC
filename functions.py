import GPUtil, wmi, psutil, platform


def get_size(bytes, suffix=""):
    factor = 1024
    for unit in ['', 'Кб', 'Мб', 'Гб', 'Тб', 'Пб']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor


def get_GPU_info():
    for gpu in GPUtil.getGPUs():
        # температура видеокарты
        GPU_temperature = f'{int(gpu.temperature)}°C'

        # загрузка видеокарты
        GPU_load = f'{int(gpu.load)}%'

        # количество использованой видеопамяти
        memory_used = f'{gpu.memoryUsed} МБ'

        # количество свободной видеопамяти
        memory_free = f'{int(gpu.memoryFree)} МБ'

        # имя видеокарты
        GPU_name = f'{gpu.name}'

    return GPU_name, GPU_temperature, GPU_load, memory_used, memory_free


def get_CPU_info():
    cpufreq = psutil.cpu_freq()

    # температура процессора
    CPU_temp = (wmi.WMI(namespace='root\\wmi').MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0) - 273.15
    CPU_temp = f'{int(CPU_temp)}°C'

    # частота процессора
    current = f'{int(cpufreq.current)}МГц'

    # имя процессора
    processor_name = f'{platform.processor()}'

    # загруженность процессора
    percent = f'{int(psutil.cpu_percent())}%'
    # количество потоков
    logical_cores = str(psutil.cpu_count(logical=True))

    # количество ядер
    cores = str(psutil.cpu_count(logical=False))

    return CPU_temp, current, processor_name, percent, logical_cores, cores


def get_RAM_info():
    # общий объём ОЗУ
    volume = f'{psutil.virtual_memory()[0] / 10 ** 9:.1f} Гб'

    # свободный объём ОЗУ
    free = f'{psutil.virtual_memory()[1] / 10 ** 9:.1f} Гб'

    # используемый объём ОЗУ
    used = f'{psutil.virtual_memory()[3] / 10 ** 9:.1f} Гб'

    return volume, free, used


def get_ROM_info():
    disk = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        disk[
            f'{partition.device[:2]}'] = f'{get_size(partition_usage.total)}', f'{get_size(partition_usage.used)}', f'{get_size(partition_usage.free)}'

    return disk


print(get_ROM_info())
# subprocess.Popen('FanControl\\FanControler\\FanControl.exe')
