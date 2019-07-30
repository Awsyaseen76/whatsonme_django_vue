<template>
  <div class="searchform">
    <h4>Find by User name</h4>
    <div class="form-group">
      <input type="text" class="form-control" id="user_name" required="" v-model="user_name" name="user_name">
    </div>
 
    <div class="btn-group">
      <button v-on:click="searchAuths" class="btn btn-success">Search</button>
    </div>
 
    <ul class="search-result">
      <li v-for="(auth, index) in auths" :key="index">
        <h6>{{auth.user_name}} ({{auth.password}})</h6>
      </li>
    </ul>
  </div>
</template>
 
<script>
import http from "../http-common";
 
export default {
  name: "search_auth",
  data() {
    return {
      user_name: '',
      auths: []
    };
  },
  methods: {
    /* eslint-disable no-console */
    searchAuths() {
      http
        .get(`/Auths/find_by_user/${this.user_name}`)
        .then(response => {
          this.auths = response.data; // JSON are parsed automatically.
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
    /* eslint-enable no-console */
  }
};
</script>
 
<style>
.searchform {
  max-width: 300px;
  margin: auto;
}
.search-result {
  margin-top: 20px;
  text-align: left;
}
</style>