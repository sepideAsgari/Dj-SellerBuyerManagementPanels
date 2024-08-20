<template>
  <!-- ggggg -->
  <div class="columns">
    <div class="column is-6">
      <div class="column gap is-11">
        <div class="grid">

          <div class="box">
            <div class="grid is-column-gap-2">
              <p class="title is-5">توجه:</p>
            </div>
            <p class="subtitle">
            <div class="grid is-column-gap-2">
              <label class="label-terms">
                با ثبت نام در سایت <a href="#">قوانین و مقررات</a> را می پزیرم.
              </label>
            </div>
            <div class="grid is-column-gap-2">
              <label class="label-terms">
                با ثبت نام در سایت <a href="#">قوانین و مقررات</a> را می پزیرم.
              </label>
            </div>
            <div class="grid is-column-gap-2">
              <label class="label-terms">
                با ثبت نام در سایت <a href="#">قوانین و مقررات</a> را می پزیرم.
              </label>
            </div>

            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="column is-6">
      <!-- <div class="column is-three-fifths is-offset-one-fifth"> -->
      <!-- <div class="grid">
        <div class="box">
          <div class="grid is-column-gap-2">
            <p class="title is-5">ورود | ثبت‌نام</p>
          </div>
          <p class="subtitle">سلام!
            <br>
            لطفا ایمیل خود را وارد کنید

          </p>
          <div class="grid is-column-gap-2">
            <div class="control has-icons-left has-icons-right">
              <input class="input is-success" type="email"> -->
      <!-- <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span> -->
      <!-- </div>
          </div>
          <div class="buttons ">
            <button class="button is-success is-fullwidth">ورود</button>
          </div>
        </div>
      </div> -->
      <div class="registration-container">
        <h1 class="title">ورود | ثبت‌نام</h1>
        <!-- <div class="field">
            <label class="label">نام کامل</label>
            <div class="control">
              <input class="input" type="text" v-model="fullName" placeholder="نام کامل">
            </div>
          </div> -->
        <div class="field">
          <label class="label">
            <p>سلام!
              <br>
              لطفا ایمیل خود را وارد کنید

            </p>
          </label>
          <div class="control">
            <input class="input" type="email" v-model="username" placeholder="company@gmail.com">
          </div>
        </div>
        <div class="field">
          <label class="label">
            <p>
              لطفا رمز عبور خود را وارد کنید
            </p>
          </label>
          <div class="control">
            <input type="password" class="input is-input-left" v-model="password" placeholder="* * * * * * * *">
          </div>
        </div>
        <!-- <div class="field">
            <label class="label">شماره تلفن</label>
            <div class="control">
              <input class="input" type="tel" pattern="[0-9]{4}[0-9]{3}[0-9]{4}" v-model="phoneNumber" placeholder="شماره تلفن">
            </div>
          </div> -->
        <!-- <div class="field">
            <label class="label">رمز عبور</label>
            <div class="control">
              <input class="input" type="password" v-model="password" placeholder="رمز عبور">
            </div>
          </div> -->
        <!-- <div class="field">
            <label class="label">تکرار رمز عبور</label>
            <div class="control">
              <input class="input" type="password" v-model="confirmPassword" placeholder="تکرار رمز عبور">
            </div>
          </div> -->
        <div class="field">
          <div class="control">
            <button class="button is-primary" @click="submitForm">ورود</button>
          </div>
        </div>
        <hr>
        <div class="field">
          <div class="label">
            یا <router-link class="has-text-link" to="/vendor/sign-up">جهت ثبت نام</router-link> کلیک کنید!
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import NoFooterMixin from '@/components/mixins/NoFooterMixin.js'

export default {
  name: 'LogIn',
  mixins: [NoFooterMixin],

  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log In | صنایع دستی'

    this.$store.commit('hideFooter')
  },
  beforeUnmount() {
    this.$store.commit('showFooter')
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")

      const formData = {
        username: this.username,
        password: this.password
      }
      console.log(formData)

      await axios
        .post("/api/v1/token/login/", formData)
        .then(response => {
          const token = response.data.auth_token

          this.$store.commit('setToken', token)

          axios.defaults.headers.common["Authorization"] = "Token " + token

          localStorage.setItem("token", token)

          const toPath = this.$route.query.to || '/vendor/dashboard'
          // const toPath = this.$route.query.to || '/sign-up'
          console.log(toPath)

          this.$router.push(toPath)
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else {
            this.errors.push('Something went wrong. Please try again')

            console.log(JSON.stringify(error))
          }
        })
    }
  }

};
</script>
<style lang="scss">
.subtitle {
  direction: rtl !important;
}

.label-terms {
  direction: rtl !important;
}

.registration-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

.registration-container h1 {
  text-align: center;
  margin-bottom: 20px;
}

.registration-container .field:not(:last-child) {
  margin-bottom: 20px;
}

.registration-container .button.is-primary {
  width: 100%;
}

// .control.has-icons-left .icon.is-left {
//   right: 0;
//}</style>