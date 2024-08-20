<template>

  <nav class="navbar" role="navigation" aria-label="main navigation">
    <!--  -->

    <!--  -->
    <!--  -->
    <div class="navbar-start">
      <div class="navbar-item">
        <a class="buttons">
          <!--  -->
          <router-link to="/cart" class="button is-success">
            <span class="icon"><i class="fas fa-shopping-cart"></i></span>
            <span> {{ cartTotalLength }}</span>
          </router-link>
          <!--  -->
          <!--  -->
          <template v-if="$store.state.isAuthenticated">
            <template v-if="this.$route.path === '/profile'">
              <router-link :to="profileLink" class="button is-light">{{ userType }}</router-link>
              <!-- <router-link to="/profile" class="button is-light" v-for="(item, index) in data" :key="index">
                {{ item }}
              </router-link> -->
            </template>
            <template v-else>
              <router-link :to="profileLink" class="button is-light">حساب کاربری</router-link>
            </template>
          </template>
          <template v-else>
            <router-link to="/log-in" class="button is-dark">ورود خریداران</router-link>
            <router-link to="/vendor/log-in" class="button is-dark">ورود فروشندگان</router-link>
            <div class="dropdown is-right is-active">
              <div class="dropdown-trigger">
                <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                  <span><i class="fa-regular fa-user" aria-hidden="true"></i></span>
                  <span class="icon is-small">
                    <i class="fa-solid fa-caret-down" aria-hidden="true"></i>
                  </span>
                </button>
              </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <a href="#" class="dropdown-item"> Dropdown item </a>
                  <a class="dropdown-item"> Other dropdown item </a>
                  <a href="#" class="dropdown-item is-active"> Active dropdown item </a>
                  <a href="#" class="dropdown-item"> Other dropdown item </a>
                  <hr class="dropdown-divider" />
                  <a href="#" class="dropdown-item"> With a divider </a>
                </div>
              </div>
            </div>
          </template>
          <!--  -->
        </a>
      </div>
    </div>

    <!--  -->
    <!--  -->
    <div class="navbar-menu-end" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
      <div id="navbarBasicExample" class="navbar-menu">
        <!--  -->
        <div class="navbar-start">
          <a class="navbar-item">
            فروشندگان
          </a>
          <a class="navbar-item">
            تماس با ما
          </a>
          <a class="navbar-item">
            درباره ما
          </a>
          <!-- <a class="navbar-item">
            کارت هدیه
          </a>
          <a class="navbar-item">
            هدایای سازمانی
          </a> -->
        </div>
        <!--  -->
      </div>
    </div>
    <!--  -->
    <!--  -->
    <div class="navbar-brand">
      <a class="navbar-item">
        <router-link to="/" class="navbar-item">
          <img width="95" src="https://yazdmemento.com/wp-content/uploads/2023/12/logo-yazd-3.svg">
        </router-link>
      </a>
    </div>
    <!--  -->
    <!--  -->
  </nav>
  <div id="wrapper">
    <!-- <nav class="navbar is-light is-hidden-desktop"> -->
    <nav class="navbar d-none d-lg-block is-light is-hidden-moblie">
      <!-- <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }"> -->

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <!-- <div class="navbar-menu">
          <div class="navbar-end">
            <router-link to="/sanaedastifelezi" class="navbar-item">صنایع دستی فلزی</router-link>
          </div>
        </div> -->
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="جستجو" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>


      <div class="navbar-end">
        <div class="navbar-item has-dropdown is-hoverable">
          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
            @click="showMobileMenu = !showMobileMenu">
            <i class="py-2 fa fa-bars"></i>
          </a>

          <a class="navbar-link">
            محصولات
          </a>
          <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
            <div class="navbar-dropdown is-right">
              <div class="item1">
                <a class="navbar-item">
                  <router-link to="/sanaedastifelezi" class="navbar-item">صنایع دستی فلزی</router-link>
                </a>
              </div>
              <div class="item1">
                <a class="navbar-item">
                  <router-link to="/sanaedastichobi" class="navbar-item">صنایع دستی چوبی</router-link>
                </a>
              </div>
              <div class="item1">
                <a class="navbar-item">
                  <router-link to="/sanaedastbaft" class="navbar-item">صنایع دست بافت</router-link>
                </a>
              </div>
              <div class="item1">
                <a class="navbar-item">
                  <router-link to="/zivaealatdastsaz" class="navbar-item">زیورآلات دست ساز</router-link>
                </a>
              </div>
              <!-- <hr class="navbar-divider"> -->
            </div>
          </div>
        </div>
      </div>
    </nav>
    <!-- <div class="navbar-brand"> -->
    <!-- <router-link to="/" class="navbar-item"><strong>صنایع دستی</strong></router-link> -->
    <!-- <a class="navbar-burger" role="button" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div> -->
    <!-- </nav> -->
    <!-- <nav class="navbar is-light">
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/sanaedastifelezi" class="navbar-item">صنایع دستی فلزی</router-link>
        </div>
      </div>
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>صنایع دستی</strong></router-link>
        <a class="navbar-burger" role="button" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
        </a>
      </div>
    </nav> -->
    <!--  -->
    <!--  -->
    <!--  -->
    <!--  -->
    <div class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>
    <section class="section pt-0" style="background-color: silver;">
      <router-view />

    </section>
    <footer v-if="showFooter">
      <Footerin />
      <!-- <p class="has-text-centered">Copyright (cccc) 2024</p>
      <Footer /> -->
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'
import Footerin from '@/components/Footerin'
// import NoFooterMixin from '@/components/mixins/NoFooterMixin.js'
import { mapState } from 'vuex'

export default {
  // mixins: [NoFooterMixin],
  data() {
    return {
      showMobileMenu: false,
      data: {},
      cart: {
        items: []
      }
    }
  },
  components: {
    Footerin
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    this.fetchUserInfo()

  },
  methods: {
    fetchUserInfo() {
      axios.get('/api/v1/get/')
        .then(response => {
          this.data = response.data;

          // Assign other user information as needed
        })
        .catch(error => {
          console.error('Error fetching user info:', error);
        });
    }
  },
  computed: {
    ...mapState(['showFooter', 'userType']),
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    },
    profileLink() {
      const currentPath = this.$route.path;

      if (currentPath.startsWith('/vendor/dashboard')) {
        return '/vendor/dashboard/profile2';
      } else if (currentPath.startsWith('/user/dashboard')) {
        return '/user/dashboard/profile2';
      } else {
        return '/';
      }
    },
  }
}
</script>


<style lang="scss">
// @import 'bulma/css/bulma.css'
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.item1 {
  direction: rtl;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
