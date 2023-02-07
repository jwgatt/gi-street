<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h1>Success</h1>
                <p>Thank you for your order!</p>
            </div>
        </div>
    </div>
</template>
<script>
export default{
    name:"Success",
    mounted(){
        document.title = "Success";
    }
}
</script>