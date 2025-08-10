const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

app.get('/check-email/:email', async (req, res) => {
    const email = req.params.email;
    try {
        const response = await axios.get(`https://www.disify.com/api/email/${email}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});