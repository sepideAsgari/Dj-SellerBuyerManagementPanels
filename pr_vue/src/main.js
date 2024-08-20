import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
// 
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";
import ArgonDashboard from "./argon-dashboard";
// 

axios.defaults.baseURL = 'http://127.0.0.1:8000'
// axios.defaults.baseURL = 'https://apiprdjango.gozarcar.ir'

createApp(App).use(store).use(router,axios).use(ArgonDashboard).mount('#app')
// createApp(App).use(store).use(router).use(ArgonDashboard).mount('#app2')
