<template>
    <section class="container">
        <div class="page-log-in">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <h1 class="title">ورود</h1>

                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <div class="labeluser">
                                <label class="label">
                                    <p>سلام!
                                        <br>
                                        لطفا ایمیل خود را وارد کنید

                                    </p>
                                </label>
                                <div class="control">
                                    <input type="text" class="input is-input-left" v-model="username"  placeholder="company@gmail.com">
                                </div>
                            </div>
                        </div>

                        <div class="field">
                            <div class="labelpass">
                                <label class="label">
                                    <p>
                                        لطفا رمز عبور خود را وارد کنید
                                    </p>
                                </label>
                                <div class="control">
                                    <input type="password" class="input is-input-left" v-model="password"
                                        placeholder="* * * * * * * *">
                                </div>
                            </div>
                        </div>

                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>

                        <div class="field">
                            <div class="control">
                                <button class="button is-medium is-fullwidth is-sinregbutton">
                                    <span class="regbuttonlabel">ورود</span>
                                </button>
                            </div>
                        </div>

                        <hr>
                        <div class="field">
                            <div class="label">
                                یا <router-link class="has-text-link" to="/sign-up">جهت ثبت نام</router-link> کلیک کنید!
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
import NoFooterMixin from '@/components/mixins/NoFooterMixin.js'

export default {
    mixins: [NoFooterMixin],

    name: 'LogIn',
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

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/'
                    // const toPath = this.$route.query.to || '/sign-up'

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

.labeluser {
    direction: rtl;
}

.labelpass {
    direction: rtl;
}

.is-input-left {
    direction: ltr;
}
</style>