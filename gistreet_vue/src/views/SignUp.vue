<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

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

                    <div class="field">
                        <label class="label">Confirm Password</label>
                        <div class="control">
                            <input class="input" type="password" v-model="password2" placeholder="Confirm Password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Sign up</button>
                        </div>
                    </div>

                    Or <router-link to="/login">login</router-link>
                 </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
    name: "SignUp",
    data() {
        return {
            username: "",
            password: "",
            password2: "",
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = [];
            if (this.password !== this.password2) {
                this.errors.push("Passwords do not match");
            }
            if (this.errors.length === 0) {
                axios.post("http://localhost:8000/api/v1/users/", {
                    username: this.username,
                    password: this.password
                }).then(response => {
                    toast({
                        message: "User created",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 5000
                    });
                    this.$router.push("/login");
                }).catch(error => {
                    if (error.response.status === 400) {
                        this.errors.push("Username already exists");
                    } else {
                        this.errors.push("Unknown error");
                    }
                });
            }
        }
    }
}
</script>