<template>
  <section class="container">
    <!-- <div class="columns is-multiline">
    <div class="column is-8 is-offset-2 register">
      <div class="columns">
        <div class="column left">
          <h1 class="title is-1">Super Cool Website</h1>
          <h2 class="subtitle colored is-4">Lorem ipsum dolor sit amet.</h2>
          <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corporis ex deleniti aliquam tempora libero
            excepturi vero soluta odio optio sed.</p>
        </div>
        <div class="column right has-text-centered">
          <h1 class="title is-4">Sign up today</h1>
          <p class="description">Lorem ipsum dolor, sit amet consectetur adipisicing elit</p>
          <form>
            <div class="field">
              <div class="control">
                <input class="input is-medium" type="text" placeholder="Name">
              </div>
            </div>

            <div class="field">
              <div class="control">
                <input class="input is-medium" type="email" placeholder="Email">
              </div>
            </div>
            <button class="button is-block is-primary is-fullwidth is-medium">Submit</button>
            <br />
            <small><em>Lorem ipsum dolor sit amet consectetur.</em></small>
          </form>
        </div>
      </div>
    </div>
    <div class="column is-8 is-offset-2">
      <br>
      <nav class="level">
        <div class="level-left">
          <div class="level-item">
            <span class="icon">
              <i class="fab fa-twitter"></i>
            </span> &emsp;
            <span class="icon">
              <i class="fab fa-facebook"></i>
            </span> &emsp;
            <span class="icon">
              <i class="fab fa-instagram"></i>
            </span> &emsp;
            <span class="icon">
              <i class="fab fa-github"></i>
            </span> &emsp;
            <span class="icon">
              <i class="fas fa-envelope"></i>
            </span>
          </div>
        </div>
        <div class="level-right">
          <small class="level-item" style="color: var(--textLight)">
            &copy; Super Cool Website. All Rights Reserved.
          </small>
        </div>
      </nav>
    </div>
  </div> -->
    <!-- </section> -->
    <div class="page-sign-up">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <h1 class="title">ثبت نام</h1>

          <form @submit.prevent="submitForm">
            <div class="field">
              <label class="label">لطفا شماره موبایل خود را وارد کنید</label>
              <div class="control">
                <input type="tel" pattern="[0-9]{4}[0-9]{3}[0-9]{4}" class="input" v-model="phonenumber"
                  placeholder="09123456789">

              </div>
            </div>

            <!-- <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div> -->

            <div class="field">
              <label class="label">لطفا ایمیل خود را وارد کنید</label>
              <div class="control">
                <input type="email" class="input" v-model="email" placeholder="company@gmail.com">

              </div>
            </div>

            <div class="field">
              <label class="label">لطفا رمز عبور خود را وارد کنید</label>
              <div class="control">
                <input type="password" class="input" v-model="password" placeholder="* * * * * * * *">
              </div>
            </div>

            <div class="field">
              <label class="label">لطفا رمز عبور خود را مجددا وارد کنید</label>
              <div class="control">
                <input type="password" class="input" v-model="password2" placeholder="* * * * * * * *">
              </div>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <div class="field">
              <div class="control">
                <button class="button is-medium is-fullwidth is-sinregbutton">
                  <span class="regbuttonlabel">ثبت نام</span>
                </button>
              </div>
            </div>

            <hr>
            <div class="field">
              <div class="label">
                یا <router-link class="has-text-link" to="/log-in">جهت ورود</router-link> کلیک کنید!
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import NoFooterMixin from '@/components/mixins/NoFooterMixin.js'

export default {
  mixins: [NoFooterMixin],

  name: 'SignUp',
  data() {
    return {
      phonenumber: '',
      username: '',
      email: '',
      password: '',
      password2: '',
      errors: []
    }
  },
  mounted() {
    this.$store.commit('hideFooter')
  },
  beforeUnmount() {
    this.$store.commit('showFooter')
  },
  methods: {
    submitForm() {
      this.errors = []

      if (this.phonenumber === '') {
        // this.errors.push('شماره موبایل نباید خالی باشد.')
        toast({
          message: 'شماره موبایل نباید خالی باشد.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
      }

      // if (this.phonenumber) {
      //   // this.errors.push('شماره موبایل تکراری می باشد.')
      //   toast({
      //     message: 'شماره موبایل تکراری می باشد.',
      //     type: 'is-warning',
      //     dismissible: true,
      //     pauseOnHover: true,
      //     duration: 3000,
      //     position: 'bottom-right',
      //   })
      // }

      if (this.email === '') {
        // this.errors.push('ایمیل نباید خالی باشد.')
        toast({
          message: 'ایمیل نباید خالی باشد.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
      }

      // if (this.email) {
      //   // this.errors.push('ایمیل تکراری می باشد.')
      //   toast({
      //     message: 'ایمیل موجود می باشد.',
      //     type: 'is-warning',
      //     dismissible: true,
      //     pauseOnHover: true,
      //     duration: 300110,
      //     position: 'bottom-right',
      //   })
      // }

      if (this.password === '') {
        // this.errors.push('رمز عبور نباید خالی باشد.')
        toast({
          message: 'رمز عبور نباید خالی باشد.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
      }

      if (this.password !== this.password2) {
        // this.errors.push('رمز عبور همخوانی ندارد.')
        toast({
          message: 'رمز عبور همخوانی ندارد.',
          type: 'is-warning',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
      }

      if (!this.errors.length) {
        const formData = {
          phonenumber: this.phonenumber,
          username: this.email,
          email: this.email,
          password: this.password
        }

        axios
          .post("/api/v1/users/", formData)
          .then(response => {
            toast({
              message: 'حساب کاربری ایجاد شد.',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: 'bottom-right',
            })

            this.$router.push('/log-in')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                if (property === 'username') {
                  toast({
                    message: `ایمیل موجود می باشد.`,
                    type: 'is-warning',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 3000,
                    position: 'bottom-right',
                  })
                } else
                  toast({
                    message: `${property}: ${error.response.data[property]}`,
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 3000,
                    position: 'bottom-right',
                  })
              }

              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Something went wrong. Please try again')

              console.log(JSON.stringify(error))
            }

          })
      }
    }
  }
}
</script>
<style lang="scss">
.label {
  direction: rtl !important;
}

.is-sinregbutton {
  background-color: #9A031E;
}

.regbuttonlabel {
  color: white !important;
}

.notification {
  direction: rtl !important;
}
</style>