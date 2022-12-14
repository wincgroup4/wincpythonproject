# Test cases for Core Banking System project

# @author: WinC Python project Group4
from server import app


def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_app_route():
    response = app.test_client().post('/app_run', follow_redirects=True)
    assert response.content_length > 0


def test_cash_route():
    response = app.test_client().get('/digital-to-cash-stats.html')
    assert response.status_code == 200


def test_report_route():
    response = app.test_client().get('/pytest-report.html')
    assert response.status_code == 200


def test_coverage_route():
    response = app.test_client().get('/code-coverage-report.html')
    assert response.status_code == 200


def test_coverage_route():
    response = app.test_client().get('/progress')
    assert response.status_code == 200
