"""
Integration tests for API endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for health endpoint"""
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


class TestChatEndpoints:
    """Tests for chat endpoints"""
    
    def test_chat_completions_missing_auth(self):
        """Test chat endpoint without auth"""
        response = client.post(
            "/api/v1/chat/completions",
            json={
                "model": "openai/gpt-4o",
                "messages": [{"role": "user", "content": "Hello!"}]
            }
        )
        
        # Should fail without API key
        assert response.status_code in [401, 422]
    
    def test_chat_completions_invalid_request(self):
        """Test chat endpoint with invalid request"""
        response = client.post(
            "/api/v1/chat/completions",
            headers={"Authorization": "Bearer test-key"},
            json={
                "model": "",
                "messages": []
            }
        )
        
        # Should fail validation
        assert response.status_code == 400


class TestModelsEndpoint:
    """Tests for models endpoint"""
    
    def test_list_models_missing_auth(self):
        """Test models endpoint without auth"""
        response = client.get("/api/v1/models")
        
        # Should fail without API key
        assert response.status_code in [401, 422]

