import scipy
import numpy as np

def initial_values() -> np.ndarray:
    H_0 = 100.0
    P_0 = 5.0
    return np.array((
        H_0,
        P_0,
    ))


def constants() -> list:
    a = 0.015
    b = 0.0125
    m = 0.8
    r = 0.2
    return [
        a,
        b,
        m,
        r,
    ]


def system(t: np.float64, y: np.ndarray, *constants) -> np.ndarray:
    H,P, = y

    a,b,m,r, = constants
    
    dH_dt = (r * H ) - (a * (H * P ) ) 
    dP_dt = ((H * P ) * b ) - (P * m ) 

    return np.array([dH_dt,dP_dt])


def simulate(st=0, tf=10, dt=0.1):
    sim_steps = np.arange(st, tf + dt, dt)

    simulation_output = scipy.integrate.solve_ivp(
        fun=system,
        t_span=(0, tf + dt),
        y0=initial_values(),
        args=constants(),
        t_eval=sim_steps,
    )

    # ...
