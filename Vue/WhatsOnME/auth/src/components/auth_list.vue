<template>
    <div class="list row">
        <div class="col-md-6">
            <h4>Auths List</h4>
            <ul>
                <li v-for="(auth, index) in auths" :key="index">
                    <router-link :to="{
                            name: 'auth_details',
                            params: { auth: auth, id: auth.id }
                        }">
                            {{auth.user_name}}
                    </router-link>
                </li>
            </ul>
        </div>
        <div class="col-md-6">
            <router-view @refreshData="refreshList"></router-view>
        </div>
    </div>    
</template>

<script>
    import http from "../http-common";
    
    export default {
        name: "authz-list",
        data() {
            return {
            auths: []
            };
        },
        methods: {
            /* eslint-disable no-console */
            retrieveAuths() {
            http
                .get("/Auths/")
                .then(response => {
                    this.auths = response.data; // JSON are parsed automatically.
                    console.log(response.data);
                })
                .catch(e => {
                    console.log(e);
                });
            },
            refreshList() {
            this.retrieveAuths();
            }
            /* eslint-enable no-console */
        },
        mounted() {
            this.retrieveAuths();
        }
    };
</script>

<style>
    .list {
        text-align: left;
        max-width: 450px;
        margin: auto;
    }
</style>
