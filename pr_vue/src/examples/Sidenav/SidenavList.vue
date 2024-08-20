<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";

import SidenavItem from "./SidenavItem.vue";
import SidenavCard from "./SidenavCard.vue";

const store = useStore();
const isRTL = computed(() => store.state.isRTL);

const getRoute = () => {
  const route = useRoute();
  const routeArr = route.path.split("/");
  return routeArr[1];
};
</script>
<template>
  <div class="collapse navbar-collapse w-auto h-auto h-100" id="sidenav-collapse-main">
    <ul class="navbar-nav">
      <li class="nav-item">
        <sidenav-item to="/vendor/dashboard" :class="getRoute() === 'dashboard-default' ? 'active' : ''"
          :navText="isRTL ? 'خلاصه فعالیت ها' : 'Dashboard'">
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item">
        <sidenav-item to="/vendor/dashboard/profile2" :class="getRoute() === 'tables' ? 'active' : ''"
          :navText="isRTL ? 'حساب کاربری' : 'Prrofile'">
          <template v-slot:icon>
            <i class="ni ni-calendar-grid-58 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item">
        <sidenav-item to="/vendor/dashboard/billing" :class="getRoute() === 'billing' ? 'active' : ''"
          :navText="isRTL ? 'کیف پول' : 'Billing'">
          <template v-slot:icon>
            <i class="ni ni-credit-card text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item">
        <sidenav-item to="/vendor/dashboard/orders" :class="getRoute() === 'billing' ? 'active' : ''"
          :navText="isRTL ? 'سفارش ها' : 'Billing'">
          <template v-slot:icon>
            <i class="fa fa-shopping-bag text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item">
        <sidenav-item to="/vendor/dashboard/comments" :class="getRoute() === 'billing' ? 'active' : ''"
          :navText="isRTL ? 'دیدگاه ها' : 'Billing'">
          <template v-slot:icon>
            <i class="fa fa-shopping-bag text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item">
        <sidenav-item to="/vendor/dashboard/comments" :class="getRoute() === 'billing' ? 'active' : ''"
          :navText="isRTL ? 'اعلان ها' : 'Billing'">
          <template v-slot:icon>
            <i class="fa fa-shopping-bag text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <!-- <li class="nav-item">
        <sidenav-item
          to="/virtual-reality"
          :class="getRoute() === 'virtual-reality' ? 'active' : ''"
          :navText="isRTL ? '' : 'Virtual Reality'"
        >
          <template v-slot:icon>
            <i class="ni ni-app text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li> -->
      <!-- 
      <li class="nav-item">
        <sidenav-item
          to="/rtl-page"
          :class="getRoute() === 'rtl-page' ? 'active' : ''"
          navText="RTL"
        >
          <template v-slot:icon>
            <i class="ni ni-world-2 text-danger text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li> -->

      <li class="mt-3 nav-item">
        <h6 v-if="isRTL" class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="isRTL ? 'me-4' : 'ms-2'">
          صفحات المرافق
        </h6>

        <h6 v-else class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6" :class="isRTL ? 'me-4' : 'ms-2'">
          ACCOUNT PAGES
        </h6>
      </li>

      <li class="nav-item">
        <sidenav-item to="/profile" :class="getRoute() === 'profile' ? 'active' : ''"
          :navText="isRTL ? 'حساب تعريفي' : 'Profile'">
          <template v-slot:icon>
            <i class="ni ni-single-02 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <!-- 
      <li class="nav-item">
        <sidenav-item
          to="/signin"
          :class="getRoute() === 'signin' ? 'active' : ''"
          :navText="isRTL ? 'تسجيل الدخول' : 'Sign In'"
        >
          <template v-slot:icon>
            <i class="ni ni-single-copy-04 text-danger text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li> -->

      <li class="nav-item">
        <sidenav-item to="/signup" :class="getRoute() === 'signup' ? 'active' : ''"
          :navText="isRTL ? 'اشتراك' : 'Sign Up'">
          <template v-slot:icon>
            <i class="ni ni-collection text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
    </ul>
  </div>

  <div class="pt-3 mx-3 mt-3 sidenav-footer">
    <sidenav-card :card="{
      title: 'Need Help?',
      description: 'Please check our docs',
      links: [
        {
          label: 'Documentation',
          route:
            'https://www.creative-tim.com/learning-lab/vue/overview/argon-dashboard/',
          color: 'dark',
        },
        {
          label: 'Buy now',
          route:
            'https://www.creative-tim.com/product/vue-argon-dashboard-pro?ref=vadp',
          color: 'success',
        },
      ],
    }" />
  </div>
</template>
