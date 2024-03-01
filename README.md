# singapore-cheap-food-api

singapore-cheap-food-api

documentation: <>

main api url: <https://asia-southeast1-singapore-cheap-food-api.cloudfunctions.net/singapore-cheap-food-api-prod-main>

findAddress api url: <https://asia-southeast1-singapore-cheap-food-api.cloudfunctions.net/singapore-cheap-food-api-prod-findAddress>

getCheapFood api url: <https://asia-southeast1-singapore-cheap-food-api.cloudfunctions.net/singapore-cheap-food-api-prod-getCheapFood>

## Requirement

- install yarn
- install node (v18)
- install python (v3.9)
- install serverless
- install gcloud cli

## Testing and run

```zsh
// get bearer token
$ gcloud auth print-identity-token

// deploy to serverless
$ yarn run deploy

// generate .serverless folder
$ yarn run package

// remove serverless services in google cloud
$ yarn run remove
```
