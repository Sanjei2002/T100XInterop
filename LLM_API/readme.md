<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# API Documentation

## 1. Get Agents List

### Endpoint

```
GET https://<domain>/getAgentslist?agentIdx=1
```


### Description

Retrieves a list of available agents with their versions.

### Request Parameters

| Parameter | Type | Required | Description |
| :-- | :-- | :-- | :-- |
| agentIdx | int | Yes | Index of the agent list to retrieve |

### Response

```json
{
    "data": [
        "1. llama2-uncensored:latest",
        "2. TX100:latest",
        "3. deepseek-r1:8b"
    ]
}
```


---

## 2. Get Prompt Response

### Endpoint

```
POST http://<domain>/getPromptResponse?agentIdx=0
```


### Description

Sends a prompt to the specified agent and receives a plain text response.

### Request

- Method: POST
- Content-Type: `multipart/form-data`
- Parameters:

| Parameter | Type | Required | Description |
| :-- | :-- | :-- | :-- |
| content | string | Yes | The prompt/question to send |

### Example cURL Request

```bash
curl --location --request POST 'http://<domain>/getPromptResponse?agentIdx=0' \
--form 'content="is 4 even?"'
```


### Response

- Content-Type: `text/plain`
- Body: Plain text containing the agent's response to the prompt.

**Example Response:**

```
Yes, 4 is an even number.
```


---

For further assistance, please contact the API support team.

