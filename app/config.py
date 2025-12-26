"""
Configuration management using Pydantic Settings
"""
from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings"""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # OpenRouter API Configuration
    openrouter_api_key: str = Field(..., description="OpenRouter API key")
    
    # Application Configuration
    app_name: str = Field(default="OpenRouter FastAPI Template", description="Application name")
    app_version: str = Field(default="1.0.0", description="Application version")
    debug: bool = Field(default=False, description="Debug mode")
    
    # Server Configuration
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    
    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(default="json", description="Log format (json or text)")
    
    # App Attribution (Optional)
    app_url: Optional[str] = Field(default=None, description="App URL for attribution")
    app_title: Optional[str] = Field(default=None, description="App title for attribution")
    
    # Rate Limiting
    rate_limit_enabled: bool = Field(default=True, description="Enable rate limiting")
    rate_limit_requests: int = Field(default=100, description="Number of requests per window")
    rate_limit_window: int = Field(default=60, description="Rate limit window in seconds")
    
    # CORS
    cors_origins: List[str] = Field(default=["*"], description="CORS allowed origins")
    cors_allow_credentials: bool = Field(default=True, description="Allow credentials in CORS")
    cors_allow_methods: List[str] = Field(default=["*"], description="CORS allowed methods")
    cors_allow_headers: List[str] = Field(default=["*"], description="CORS allowed headers")
    
    # File Upload Limits
    max_file_size: int = Field(default=52428800, description="Max file size in bytes (50MB)")
    max_video_size: int = Field(default=104857600, description="Max video size in bytes (100MB)")
    
    # Monitoring
    enable_metrics: bool = Field(default=True, description="Enable metrics collection")
    enable_tracing: bool = Field(default=False, description="Enable distributed tracing")
    
    # OpenRouter API
    openrouter_base_url: str = Field(
        default="https://openrouter.ai/api/v1",
        description="OpenRouter API base URL"
    )
    openrouter_timeout: float = Field(default=30.0, description="Request timeout in seconds")
    openrouter_max_retries: int = Field(default=3, description="Maximum retry attempts")


# Global settings instance
settings = Settings()

