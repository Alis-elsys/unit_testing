import nox

@nox.session(name = "proba", python=["3.8.2"])
def tests(session):
    session.install("pytest")
    session.run("pytest", "-v", "tests.py")
    session.run("python", "main.py")
