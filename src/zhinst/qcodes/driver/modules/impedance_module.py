"""Autogenerated module for the ImpedanceModule QCoDeS driver."""
import typing as t
from typing import Optional
from zhinst.toolkit.driver.modules.impedance_module import (
    ImpedanceModule as TKImpedanceModule,
)

from zhinst.qcodes.driver.modules.base_module import ZIBaseModule


if t.TYPE_CHECKING:
    from zhinst.qcodes.session import Session


class ZIImpedanceModule(ZIBaseModule):
    """Implements a base Impedance Module for Lock-In instruments.

    The Impedance Module corresponds to the Cal sub-tab in the LabOne User
    Interface Impedance Analyzer tab. It allows the user to perform a
    compensation that will be applied to impedance measurements.

    For a complete documentation see the LabOne user manual
    https://docs.zhinst.com/labone_programming_manual/impedance_module.html


    Args:
        tk_object: Underlying zhinst-toolkit object.
        session: Session to the Data Server.
        name: Name of the module in QCoDeS.
    """

    def __init__(
        self,
        tk_object: TKImpedanceModule,
        session: "Session",
        name: str = "impedance_module",
    ):
        super().__init__(tk_object, session, name)

    def wait_done(
        self,
        step: Optional[int] = None,
        *,
        timeout: float = 20.0,
        sleep_time: float = 0.5,
    ) -> None:
        """Waits until the specified compensation step is complete.

        Args:
            step: The compensation step to wait for completion.
            timeout: The maximum waiting time in seconds for the compensation
                to complete (default: 20).
            sleep_time: Time in seconds to wait between
                requesting the state. (default: 0.5)

        Raises:
            TimeoutError: The compensation is not completed before timeout.
        """
        return self._tk_object.wait_done(
            step=step, timeout=timeout, sleep_time=sleep_time
        )

    def finish(self) -> None:
        """Stop the module."""
        return self._tk_object.finish()

    def finished(self, step: Optional[int] = None) -> bool:
        """Check if the calibration or a step of it is finished.

        Args:
            step: Calibration step. If not None this function checks if the
                specified step is finished. Otherwise it checks if the
                hole calibration is done.

        Returns:
            Flag if the calibration or a step is finished.
        """
        return self._tk_object.finished(step=step)
