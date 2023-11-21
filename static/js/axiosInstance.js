const accessToken = getCookie("access");

let headers = {
    'X-CSRFToken': getCookie('csrftoken')
}

if (accessToken) {
    headers['Authorization'] = `Bearer ${accessToken}`; 
}
const axiosInstance = axios.create({
    baseURL: '/',
    headers: headers
})
