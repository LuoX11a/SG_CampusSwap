"""
Tests for application configuration.
"""

from app.config import Settings, settings


class TestSettingsDefaults:
    """Default configuration values should be set correctly."""

    def test_app_name_default(self):
        s = Settings()
        assert s.APP_NAME == "SG CampusSwap API"

    def test_app_version_default(self):
        s = Settings()
        assert s.APP_VERSION == "1.0.0"

    def test_environment_default(self):
        s = Settings()
        assert s.ENVIRONMENT == "development"

    def test_api_v1_prefix_default(self):
        s = Settings()
        assert s.API_V1_PREFIX == "/api/v1"

    def test_jwt_algorithm_default(self):
        s = Settings()
        assert s.JWT_ALGORITHM == "HS256"

    def test_access_token_expiry_default(self):
        s = Settings()
        assert s.ACCESS_TOKEN_EXPIRE_MINUTES == 30

    def test_refresh_token_expiry_default(self):
        s = Settings()
        assert s.REFRESH_TOKEN_EXPIRE_DAYS == 7

    def test_cors_origins_default(self):
        """CORS_ORIGINS class default is '*' (env may override)."""
        import os

        old_val = os.environ.pop("CORS_ORIGINS", None)
        try:
            s = Settings(_env_file=None)  # skip .env file
            assert s.CORS_ORIGINS == "*"
        finally:
            if old_val is not None:
                os.environ["CORS_ORIGINS"] = old_val


class TestAllowedDomainsList:
    """The allowed_domains_list property should parse the comma-separated string."""

    def test_returns_list(self):
        result = settings.allowed_domains_list
        assert isinstance(result, list)

    def test_not_empty(self):
        result = settings.allowed_domains_list
        assert len(result) > 0

    def test_contains_nus_domains(self):
        result = settings.allowed_domains_list
        assert "u.nus.edu" in result
        assert "nus.edu.sg" in result

    def test_contains_ntu_domains(self):
        result = settings.allowed_domains_list
        assert "e.ntu.edu.sg" in result
        assert "ntu.edu.sg" in result

    def test_no_empty_strings(self):
        result = settings.allowed_domains_list
        assert all(d != "" for d in result)
