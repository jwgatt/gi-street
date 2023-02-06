<template>
    <div class="login-page">
        <div class="columns">
            <div class="colums is-4 is-offset-4">
                <h1 class="title">Login</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Username</label>
                        <div class="control">
                            <input class="input" type="text" v-model="username" placeholder="Username">
                        </div>
                    </div>
                
                    <div class="field">
                        <label class="label">Password</label>
                        <div class="control">
                            <input class="input" type="password" v-model="password" placeholder="Password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Login</button>
                        </div>
                    </div>

                    <hr>
                    Or <router-link to="/signup">sign up</router-link>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";
export default{
    name: "Login",
    data() {
        return {
            username: "",
            password: "",
            errors: []
        }
    },
    mounted() {
        document.title = "Login | Gistreet";
    },
    methods:{
        async submitForm(){
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            const FormData = {
                username: this.username,
                password: this.password
            }

            await axios.post("/api/v1/token/login/", FormData)
             .then(response => {
             const token = response.data.auth_token

             //call store for info fromserver
             this.$store.commit('setToken', token)

             //set header for persistent login
             axios.defaults.headers.common['Authorization'] = 'Token ' + token

             //store in local so user can stay logged in on refresh
             localStorage.setItem('token', token)

             //redirect to cart page or to page user was on
             const toPath= this.$route.query.to || '/cart'

             //redirect to cart page when you sign in
             this.$router.push(toPath)
            })
            .catch(error=>{
                if (error.response) {
                    for(const property in error.response.data){
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                }else{
                    this.errors.push("Something went wrong. Please try again later.")

                    console.log(JSON.stringify(error))
                }
            })
        }
}}
</script>