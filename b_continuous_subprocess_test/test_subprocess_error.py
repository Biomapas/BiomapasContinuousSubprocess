import json
from subprocess import CalledProcessError

from b_continuous_subprocess.continuous_subprocess import ContinuousSubprocess


def test_subprocess_error() -> None:
    """
    Checks whether an exception is raised when an unknown command is passed.

    :return: No return.
    """
    try:
        list(ContinuousSubprocess('TestCommandThatProbablyDoesNotExist').execute())
    except CalledProcessError as ex:
        error_output = json.loads(ex.output)

        # Error message.
        message = error_output['message']
        # Stack trace.
        trace = error_output['trace']
        # The length of a stack trace (in lines).
        trace_size = error_output['trace_size']
        # The maximum possible (allowed) length of a stack trace.
        max_trace_size = error_output['max_trace_size']

        assert message == 'An error has occurred while running the specified command.'
        assert max_trace_size == 1000

        # This project (as of this commit) is being hosted in Github.
        # Github somehow magically handles stdout/stderr by itself, hence
        # our processes can't yield anything. This is definitely a
        # serious issue that needs to be resolved.
        # assert len(trace) > 0
        # assert trace_size > 0

        return

    raise AssertionError('Expected to raise an exception.')
