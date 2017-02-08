<template lang="html">
    <div class="ui container main">
        <transition name="fade">
          <router-view></router-view>
        </transition>
    </div>
</template>

<style>
.ui.container.main {
  padding-top: 35px;
  padding-bottom: 35px;
}
</style>
