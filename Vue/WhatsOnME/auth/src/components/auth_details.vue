<template>
  <div v-if="this.auth">
    <h4>Auth</h4>
    <div>
      <label>User name: </label> {{this.auth.user_name}}
    </div>
    <div>
      <label>Password: </label> {{this.auth.password}}
    </div>
    <!-- <span class="button btn-danger" v-on:click="deleteAuth()">Delete</span> -->
    <b-button variant="danger" v-on:click="deleteAuth()">Delete</b-button>
  </div>
  <div v-else="">
    <br>
    <p>Please click on Auth...</p>
  </div>
</template>
 
<script>
  import http from "../http-common";
 
  export default {
    name: "auth_details",
    props: ["auth"],
    methods: {
      /* eslint-disable no-console */
      deleteAuth() {
        http
          .delete("/Auths/" + this.auth.id)
          .then(response => {
            console.log(response.data);
            this.$emit("refreshData");
            this.$router.push('/');
          })
          .catch(e => {
            console.log(e);
          });
      }
      /* eslint-enable no-console */
    }
  };
</script>