#!/usr/bin/python3
import sys
import psutil
import platform


def cpu_info():
    cpu_percent = psutil.cpu_times_percent()
    idle = cpu_percent.idle
    print('system.cpu.idle %s' % idle)
    user = cpu_percent.user
    print('system.cpu.user %s' % user)
    guest = cpu_percent.guest
    print('system.cpu.guest %s' % guest)
    iowait = cpu_percent.iowait
    print('system.cpu.iowait %s' % iowait)
    steal = cpu_percent.steal
    print('system.cpu.steal %s' % steal)
    system = cpu_percent.system
    print('system.cpu.system %s' % system)


def memory_info():
    mem_percent = psutil.virtual_memory()
    mem_swap = psutil.swap_memory()
    virtual_total = mem_percent.total
    print('virtual total %s ' % virtual_total)
    virtual_used = mem_percent.used
    print('virtual used %s ' % virtual_used)
    virtual_free = mem_percent.free
    print('virtual free %s ' % virtual_free)
    virtual_shared = mem_percent.shared
    print('virtual shared %s ' % virtual_shared)
    swap_total = mem_swap.total
    print('swap total %s ' % swap_total)
    swap_used = mem_swap.used
    print('swap used %s ' % swap_used)
    swap_free = mem_swap.free
    print('swap free %s ' % swap_free)


if __name__ == "__main__":
    os, name, version, _, _, _ = platform.uname()
    version = version.split('-')[0]
    cores = psutil.cpu_count()
    print("I am currently running on %s version %s.  " % (os, version))
    print("This system is named %s and has %s CPU cores.  " % (name, cores))

    try:
        if len(sys.argv) > 2:
            print("Wrong amount of parameters. Just only one.")
        elif sys.argv[1] == 'cpu':
            cpu_info()
        elif sys.argv[1] == 'mem':
            memory_info()
        else:
            print("You can use only one parameter in range [mem, cpu]")
    except IndexError:
        print("IndexError: list index out of range")
        print("You can use only one parameter mem or cpu")
