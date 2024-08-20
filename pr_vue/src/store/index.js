import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    user: null,
    userType: '',
    token: '',
    isLoading: false,
    showFooter: true,
    // 
    hideConfigButton: false,
    isPinned: false,
    showConfig: false,
    sidebarType: "bg-white",
    isRTL: true,
    mcolor: "",
    darkMode: false,
    isNavFixed: false,
    isAbsolute: false,
    showNavs: true,
    showSidenav: true,
    showNavbar: true,
    showFooter: true,
    showMain: true,
    layout: "default",
    // 
  },
  mutations: {
    setUser(state, user) {
      state.user = user
      state.isAuthenticated = true
      state.userType = user.userType
    },
    // logout(state) {
    //   state.user = null;
    //   state.isAuthenticated = false;
    // },
    hideFooter(state) {
      state.showFooter = false
    },
    showFooter(state) {
      state.showFooter = true
    },
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    setUserType(state, userType) {
      state.userType = userType
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
      state.user = null
      state.userType = ''
    },
    clearCart(state) {
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    clearCartLen(state) {
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    toggleConfigurator(state) {
      state.showConfig = !state.showConfig;
    },
    sidebarMinimize(state) {
      let sidenav_show = document.querySelector("#app");
      if (state.isPinned) {
        sidenav_show.classList.add("g-sidenav-hidden");
        sidenav_show.classList.remove("g-sidenav-pinned");
        state.isPinned = false;
      } else {
        sidenav_show.classList.add("g-sidenav-pinned");
        sidenav_show.classList.remove("g-sidenav-hidden");
        state.isPinned = true;
      }
    },
    sidebarType(state, payload) {
      state.sidebarType = payload;
    },
    navbarFixed(state) {
      if (state.isNavFixed === false) {
        state.isNavFixed = true;
      } else {
        state.isNavFixed = false;
      }
    },
  },
  actions: {
    async fetchUser({ commit }, token) {
      try {
        const response = await axios.get('/api/v1/user-info/', {
          headers: { 'Authorization': `Token ${token}` }
        });
        commit('setUser', response.data);
      } catch (error) {
        console.error('Error fetching user info:', error);
      }
    },

    toggleSidebarColor({ commit }, payload) {
      commit("sidebarType", payload);
    },
    login({ commit }, user) {
      // فرض کنید این متد پس از موفقیت آمیز بودن احراز هویت فراخوانی می‌شود
      commit('setUser', user);
    },
  },
  modules: {
  },
  getters: {
    isVendor: state => state.user && state.user.userType === 'vendor',
    isCustomer: state => state.user && state.user.userType === 'customer',
  },
});