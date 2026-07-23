"""
SG CampusSwap — Application Configuration.
Loaded from environment variables with pydantic-settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Application ──────────────────────────────────────
    APP_NAME: str = "SG CampusSwap API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    # ── Database ─────────────────────────────────────────
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/sg_campusswap"
    DATABASE_URL_SYNC: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/sg_campusswap"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20

    # ── JWT ──────────────────────────────────────────────
    JWT_SECRET: str = "change-me-in-production-use-openssl-rand-hex-32"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # ── University Email Domain Whitelist ─────────────────
    ALLOWED_EMAIL_DOMAINS: str = (
        # Singapore public universities
        "u.nus.edu,nus.edu.sg,nus.edu,"
        "e.ntu.edu.sg,ntu.edu.sg,"
        "smu.edu.sg,sutd.edu.sg,suss.edu.sg,sit.edu.sg,singaporetech.edu.sg,"
        # Singapore polytechnics
        "connect.np.edu.sg,np.edu.sg,"
        "ichat.sp.edu.sg,sp.edu.sg,"
        "tp.edu.sg,nyp.edu.sg,rp.edu.sg,"
        # Singapore arts institutions
        "lasalle.edu.sg,nafa.edu.sg,"
        # Singapore private institutions
        "mymail.sim.edu.sg,sim.edu.sg,"
        "kaplan.edu.sg,psb-academy.edu.sg,curtin.edu.sg,mdis.edu.sg,raffles.edu.sg,"
        "jcu.edu.sg,my.jcu.edu.au,"
        # International universities with Singapore campuses
        "insead.edu,digipen.edu,essec.edu,"
        "amity.edu,s.amity.edu,"
        "coventry.ac.uk,gla.ac.uk,"
        "tum.de,tum-asia.edu.sg"
    )

    # ── Email Verification ────────────────────────────────
    SMTP_HOST: str = "smtp.sendgrid.net"
    SMTP_PORT: int = 587
    SMTP_USER: str = "apikey"
    SMTP_PASS: str = ""
    SMTP_FROM: str = "noreply@sgcampusswap.com"
    VERIFICATION_CODE_LENGTH: int = 6
    VERIFICATION_CODE_EXPIRE_MINUTES: int = 10

    # ── Firebase ─────────────────────────────────────────
    FIREBASE_SERVICE_ACCOUNT_PATH: str = "firebase-service-account.json"

    # ── Cloudinary ───────────────────────────────────────
    CLOUDINARY_CLOUD_NAME: str = ""
    CLOUDINARY_API_KEY: str = ""
    CLOUDINARY_API_SECRET: str = ""
    CLOUDINARY_MAX_FILE_SIZE_MB: int = 5

    # ── AWS ──────────────────────────────────────────────
    AWS_REGION: str = "ap-southeast-1"

    # ── CORS ─────────────────────────────────────────────
    CORS_ORIGINS: str = "*"

    @property
    def allowed_domains_list(self) -> list[str]:
        """Return the email domain whitelist as a list."""
        return [d.strip() for d in self.ALLOWED_EMAIL_DOMAINS.split(",") if d.strip()]


settings = Settings()
