import axios from 'axios'

export const AXIOS = axios.create({
    baseURL : 'http://localhost:5000',
    timeout: 10000,
})