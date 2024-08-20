import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/HomeView.vue'
import NotFound from '../views/NotFound.vue';

import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Profile from '../views/Profile.vue'
import Orders from '../views/Oeders.vue'
import DashBoard from '../views/Dashboard.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'

// seller
// import SellerLogin from '@/views/seller/SellerLogin.vue'
import VendorLogIn from '../views/vendor/VendorLogIn.vue'
import VendorSignUp from '../views/vendor/VendorSignUp.vue'
import VendorDashBoard from '../views/vendor/VendorDashBoard.vue'
// import VendorReCover from '../views/vendor/VendorReCover.vue'

// vendor
import Dashboard2 from "../views/Dashboard2.vue";
import Tables from "../views/Tables.vue";
import Billing from "../views/Billing.vue";
import VendorOrders from "../views/Vendororders.vue";
import VendorComments from "../views/Vendorcomments.vue";
// import VirtualReality from "../views/VirtualReality.vue";
import RTL from "../views/Rtl.vue";
import Profile2 from "../views/Profile2.vue";
// import Signup from "../views/Signup.vue";
// import Signin from "../views/Signin.vue";


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/orders',
    name: 'Orders',
    component: Orders,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashBoard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },
  // vendor
  {
    path: '/vendor/log-in',
    name: 'VendorLogIn',
    component: VendorLogIn
  },
  {
    path: '/vendor/sign-up',
    name: 'VendorSignUp',
    component: VendorSignUp
  },
  {
    path: '/vendor/dashboard/dashboard-default',
    name: 'VendorDashBoard',
    component: VendorDashBoard
  },
  {
    path: "/vendor/dashboard",
    name: "Dashboard2",
    component: Dashboard2,
  },
  {
    path: "/vendor/dashboard/tables",
    name: "Tables",
    component: Tables,
  },
  {
    path: "/vendor/dashboard/billing",
    name: "Billing",
    component: Billing,
  },
  {
    path: "/vendor/dashboard/orders",
    name: "Vendororders",
    component: VendorOrders,
  },
  {
    path: "/vendor/dashboard/comments",
    name: "Vendorcomments",
    component: VendorComments,
  },
  {
    path: "/vendor/dashboard/rtl-page",
    name: "RTL",
    component: RTL,
  },
  {
    path: "/vendor/dashboard/profile2",
    name: "Profile2",
    component: Profile2,
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  // 
  linkActiveClass: "active"
  // 
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router;