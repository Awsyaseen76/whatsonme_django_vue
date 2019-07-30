<template>
  <div class="submitform">
    <div v-if="!submitted">
        <div class="form-group">
          <label for="user_name">User name</label>
          <input type="text" class="form-control" id="user_name" required="" v-model="auth.user_name" name="user_name">
        </div>
    
        <div class="form-group">
          <label for="age">Password</label>
          <input type="text" class="form-control" id="password" required="" v-model="auth.password" name="password">
        </div>
    
        <button v-on:click="saveAuth" class="btn btn-success">Submit</button>
    </div>
    
    <div v-else="">
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" v-on:click="newAuth">Add</button>
    </div>
  </div>
</template>
 
<script>
import http from "../http-common";
 
export default {
  name: "add_auth",
  data() {
    return {
      auth: {
        id: 0,
        user_name: "",
        password: '',
        createdAt: null,
        updatedAt: null
      },
      submitted: false
    };
  },
  methods: {
    /* eslint-disable no-console */
    saveAuth() {
      var data = {
        user_name: this.auth.user_name,
        password: this.auth.password
      };
 
      http
        .post("/Auths/", data)
        .then(response => {
          this.auth.id = response.data.id;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
 
      this.submitted = true;
    },
    newAuth() {
      this.submitted = false;
      this.auth = {};
    }
    /* eslint-enable no-console */
  }
};
</script>
 
<style>
    .submitform {
    max-width: 300px;
    margin: auto;
    }
</style>