
let headers = {
    'X-CSRFToken': getCookie('csrftoken')
}


const axiosInstance = axios.create({
    baseURL: '/',
    headers: headers
})