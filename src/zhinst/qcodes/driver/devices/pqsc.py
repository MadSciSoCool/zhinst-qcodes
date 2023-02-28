"""Autogenerated module for the PQSC QCoDeS driver."""
from typing import List, Union
from zhinst.qcodes.driver.devices.base import ZIBaseInstrument


class PQSC(ZIBaseInstrument):
    """QCoDeS driver for the Zurich Instruments PQSC."""

    def _init_additional_nodes(self):
        """Init class specific modules and parameters."""

    def arm(self, *, deep=True, repetitions: int = None, holdoff: float = None) -> None:
        """Prepare PQSC for triggering the instruments.

        This method configures the execution engine of the PQSC and
        clears the register bank. Optionally, the *number of triggers*
        and *hold-off time* can be set when specified as keyword
        arguments. If they are not specified, they are not changed.

        Note that the PQSC is disabled at the end of the hold-off time
        after sending out the last trigger. Therefore, the hold-off time
        should be long enough such that the PQSC is still enabled when
        the feedback arrives. Otherwise, the feedback cannot be processed.

        Args:
            deep: A flag that specifies if a synchronization
                should be performed between the device and the data
                server after stopping the PQSC and clearing the
                register bank (default: True).
            repetitions: If specified, the number of triggers sent
                over ZSync ports will be set (default: None).
            holdoff: If specified, the time between repeated
                triggers sent over ZSync ports will be set. It has a
                minimum value and a granularity of 100 ns
                (default: None).

        """
        return self._tk_object.arm(deep=deep, repetitions=repetitions, holdoff=holdoff)

    def run(self, *, deep: bool = True) -> None:
        """Start sending out triggers.

        This method activates the trigger generation to trigger all
        connected instruments over ZSync ports.

        Args:
            deep: A flag that specifies if a synchronization
                should be performed between the device and the data
                server after enabling the PQSC (default: True).

        """
        return self._tk_object.run(deep=deep)

    def arm_and_run(self, *, repetitions: int = None, holdoff: float = None) -> None:
        """Arm the PQSC and start sending out triggers.

        Simply combines the methods arm and run. A synchronization
        is performed between the device and the data server after
        arming and running the PQSC.

        Args:
            repetitions: If specified, the number of triggers sent
                over ZSync ports will be set (default: None).
            holdoff: If specified, the time between repeated
                triggers sent over ZSync ports will be set. It has a
                minimum value and a granularity of 100 ns
                (default: None).

        """
        return self._tk_object.arm_and_run(repetitions=repetitions, holdoff=holdoff)

    def stop(self, *, deep: bool = True) -> None:
        """Stop the trigger generation.

        Args:
            deep: A flag that specifies if a synchronization
                should be performed between the device and the data
                server after disabling the PQSC (default: True).

        """
        return self._tk_object.stop(deep=deep)

    def wait_done(self, *, timeout: float = 10, sleep_time: float = 0.005) -> None:
        """Wait until trigger generation and feedback processing is done.

        Args:
            timeout: The maximum waiting time in seconds for the
                PQSC (default: 10).
            sleep_time: Time in seconds to wait between
                requesting PQSC state

        Raises:
            TimeoutError: If the PQSC is not done sending out all
                triggers and processing feedback before the timeout.
        """
        return self._tk_object.wait_done(timeout=timeout, sleep_time=sleep_time)

    def check_ref_clock(self, *, timeout: int = 30, sleep_time: int = 1) -> bool:
        """Check if reference clock is locked successfully.

        Args:
            timeout: Maximum time in seconds the program waits
                (default: 30).
            sleep_time: Time in seconds to wait between
                requesting the reference clock status (default: 1)

        Raises:
            TimeoutError: If the process of locking to the reference clock
                exceeds the specified timeout.
        """
        return self._tk_object.check_ref_clock(timeout=timeout, sleep_time=sleep_time)

    def check_zsync_connection(
        self,
        ports: Union[List[int], int] = 0,
        *,
        timeout: int = 30,
        sleep_time: int = 1,
    ) -> Union[List[bool], bool]:
        """Check if the ZSync connection on the given port(s) is established.

        This function checks the current status of the instrument connected to
        the given ports.

        Args:
            ports: The port numbers to check the ZSync connection for.
                It can either be a single port number given as integer or a list
                of several port numbers. (default: 0)
            timeout: Maximum time in seconds the program waits (default: 30).
            sleep_time: Time in seconds to wait between requesting the reference
                clock status (default: 1)

        Raises:
            TimeoutError: If the process of establishing a ZSync connection on
                one of the specified ports exceeds the specified timeout.
        """
        return self._tk_object.check_zsync_connection(
            ports=ports, timeout=timeout, sleep_time=sleep_time
        )

    def find_zsync_worker_port(self, device: ZIBaseInstrument) -> int:
        """Find the ID of the PQSC ZSync port connected to a given device.

        Args:
            pqsc: PQSC device over whose ports the research shall be done.
            device: device for which the connected ZSync port shall be found.

        Returns:
            Integer value represent the ID of the searched PQSC Zsync port.

        Raises:
            ToolkitError: If the given device doesn't appear to be connected
                to the PQSC via ZSync.

        .. versionadded:: 0.5.1
        """
        return self._tk_object.find_zsync_worker_port(device=device._tk_object)
